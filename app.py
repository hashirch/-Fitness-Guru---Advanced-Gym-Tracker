from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, ConnectionFailure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import os
import logging
from werkzeug.exceptions import HTTPException
from werkzeug.security import safe_join

from utils import (
    calculate_bmi, calculate_bmr, calculate_tdee, get_bmi_category,
    hash_password, verify_password, validate_email, validate_username,
    calculate_workout_volume, calculate_one_rep_max, format_duration,
    get_workout_difficulty_rating, calculate_streak_days, sanitize_input,
    validate_workout_data
)
import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config.config[config_name])

# Initialize database connection
try:
    client = MongoClient(app.config['MONGO_URI'])
    db = client[app.config['DB_NAME']]
    users_col = db['users']
    logs_col = db['logs']
    
    # Create indexes for better performance
    users_col.create_index("email", unique=True)
    logs_col.create_index([("user_id", 1), ("date", -1)])
    
    logger.info("Database connection established successfully")
except ConnectionFailure as e:
    logger.error(f"Failed to connect to database: {e}")
    raise

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('errors/error.html', error=e), e.code

# Authentication decorator
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Routes
@app.route('/')
def index():
    logged_in = 'user_id' in session
    user_id = session.get('user_id', None)
    
    if logged_in:
        # Get user stats for dashboard
        try:
            user_data = users_col.find_one({"_id": user_id})
            recent_workouts = list(logs_col.find({"user_id": user_id}).sort("date", -1).limit(5))
            
            # Calculate streak
            workout_dates = [log['date'] for log in logs_col.find({"user_id": user_id}, {"date": 1})]
            streak = calculate_streak_days(workout_dates)
            
            return render_template('index.html', 
                                logged_in=logged_in, 
                                user_id=user_id,
                                user_data=user_data,
                                recent_workouts=recent_workouts,
                                streak=streak)
        except Exception as e:
            logger.error(f"Error loading dashboard data: {e}")
            flash('Error loading dashboard data.', 'error')
    
    return render_template('index.html', logged_in=logged_in, user_id=user_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = sanitize_input(request.form.get('username', ''))
            email = request.form.get('email', '').lower().strip()
            password = request.form.get('password', '')
            confirm_password = request.form.get('confirm_password', '')
            
            # Validation
            errors = []
            
            # Username validation
            is_valid_username, username_msg = validate_username(username)
            if not is_valid_username:
                errors.append(username_msg)
            
            # Email validation
            if not validate_email(email):
                errors.append("Please enter a valid email address")
            
            # Password validation
            if len(password) < 6:
                errors.append("Password must be at least 6 characters long")
            elif password != confirm_password:
                errors.append("Passwords do not match")
            
            if errors:
                for error in errors:
                    flash(error, 'error')
                return render_template('register.html')
            
            # Check if user already exists
            if users_col.find_one({"$or": [{"_id": username}, {"email": email}]}):
                flash('Username or email already exists!', 'error')
                return render_template('register.html')
            
            # Create user
            hashed_password = hash_password(password)
            user_data = {
                "_id": username,
                "email": email,
                "password": hashed_password,
                "created_at": datetime.datetime.now(),
                "last_login": datetime.datetime.now()
            }
            
            users_col.insert_one(user_data)
            session['user_id'] = username
            flash('Registration successful! Welcome to Fitness Guru!', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            logger.error(f"Registration error: {e}")
            flash('An error occurred during registration. Please try again.', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = sanitize_input(request.form.get('username', ''))
            password = request.form.get('password', '')
            
            if not username or not password:
                flash('Please enter both username and password.', 'error')
                return render_template('login.html')
            
            user = users_col.find_one({"_id": username})
            if user and verify_password(password, user['password']):
                session['user_id'] = username
                
                # Update last login
                users_col.update_one(
                    {"_id": username},
                    {"$set": {"last_login": datetime.datetime.now()}}
                )
                
                flash(f'Welcome back, {username}!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password.', 'error')
                
        except Exception as e:
            logger.error(f"Login error: {e}")
            flash('An error occurred during login. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user_id = session['user_id']
    
    if request.method == 'POST':
        try:
            age = int(request.form.get('age', 0))
            weight = float(request.form.get('weight', 0))
            height = float(request.form.get('height', 0))
            gender = request.form.get('gender', '').lower()
            goal = request.form.get('goal', '')
            activity_level = request.form.get('activity_level', 'moderate')
            
            # Validation
            if age < 13 or age > 120:
                flash('Please enter a valid age between 13 and 120.', 'error')
                return redirect(url_for('profile'))
            
            if weight < 30 or weight > 300:
                flash('Please enter a valid weight between 30 and 300 kg.', 'error')
                return redirect(url_for('profile'))
            
            if height < 100 or height > 250:
                flash('Please enter a valid height between 100 and 250 cm.', 'error')
                return redirect(url_for('profile'))
            
            if gender not in ['male', 'female']:
                flash('Please select a valid gender.', 'error')
                return redirect(url_for('profile'))
            
            # Calculate metrics
            bmi = calculate_bmi(weight, height)
            bmr = calculate_bmr(weight, height, age, gender)
            tdee = calculate_tdee(bmr, activity_level)
            bmi_category, bmi_advice = get_bmi_category(bmi)
            
            # Update user profile
            profile_data = {
                "age": age,
                "weight": weight,
                "height": height,
                "gender": gender,
                "goal": goal,
                "activity_level": activity_level,
                "bmi": bmi,
                "bmr": bmr,
                "tdee": tdee,
                "bmi_category": bmi_category,
                "bmi_advice": bmi_advice,
                "updated_at": datetime.datetime.now()
            }
            
            users_col.update_one(
                {"_id": user_id},
                {"$set": profile_data},
                upsert=True
            )
            
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('profile'))
            
        except ValueError as e:
            flash(str(e), 'error')
        except Exception as e:
            logger.error(f"Profile update error: {e}")
            flash('An error occurred while updating your profile.', 'error')
    
    # Get existing user data
    user_data = users_col.find_one({"_id": user_id})
    return render_template('profile.html', user_id=user_id, user_data=user_data)

@app.route('/log', methods=['GET', 'POST'])
@app.route('/workout', methods=['GET', 'POST'])
@login_required
def log_workout():
    user_id = session['user_id']
    
    if request.method == 'POST':
        try:
            workout = sanitize_input(request.form.get('workout', ''))
            duration = int(request.form.get('duration', 0))
            reps = int(request.form.get('reps', 0))
            sets = int(request.form.get('sets', 0))
            difficulty = int(request.form.get('difficulty', 3))
            weight = float(request.form.get('weight', 0)) if request.form.get('weight') else None
            notes = sanitize_input(request.form.get('notes', ''))
            
            # Validate workout data
            errors = validate_workout_data(workout, duration, reps, sets, difficulty)
            if errors:
                for error in errors:
                    flash(error, 'error')
                return render_template('log_workout.html', user_id=user_id)
            
            # Get user data for BMI calculation
            user = users_col.find_one({"_id": user_id})
            if not user or 'weight' not in user or 'height' not in user:
                flash('Please complete your profile first to log workouts.', 'error')
                return redirect(url_for('profile'))
            
            bmi = calculate_bmi(user['weight'], user['height'])
            volume = calculate_workout_volume(sets, reps, weight)
            one_rep_max = calculate_one_rep_max(weight, reps) if weight else None
            
            # Create workout log
            log_data = {
                "user_id": user_id,
                "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                "workout": workout,
                "duration_mins": duration,
                "reps": reps,
                "sets": sets,
                "weight": weight,
                "volume": volume,
                "one_rep_max": one_rep_max,
                "difficulty_rating": difficulty,
                "notes": notes,
                "bmi": bmi,
                "created_at": datetime.datetime.now()
            }
            
            logs_col.insert_one(log_data)
            flash('Workout logged successfully!', 'success')
            return redirect(url_for('progress'))
            
        except ValueError as e:
            flash(str(e), 'error')
        except Exception as e:
            logger.error(f"Workout logging error: {e}")
            flash('An error occurred while logging your workout.', 'error')
    
    return render_template('log_workout.html', user_id=user_id)

@app.route('/progress')
@login_required
def progress():
    user_id = session['user_id']
    
    try:
        # Get user's workout logs
        logs = list(logs_col.find({"user_id": user_id}).sort("date", 1))
        
        if not logs:
            return render_template('progress.html', user_id=user_id, has_data=False)
        
        # Prepare data for charts
        dates = [log['date'] for log in logs]
        bmi_values = [log.get('bmi', 0) for log in logs]
        volumes = [log.get('volume', 0) for log in logs]
        
        # Calculate statistics
        total_workouts = len(logs)
        avg_duration = sum(log.get('duration_mins', 0) for log in logs) / total_workouts
        total_volume = sum(volumes)
        
        # Create charts directory
        static_dir = os.path.join(app.root_path, 'static')
        graphs_dir = os.path.join(static_dir, 'graphs')
        os.makedirs(graphs_dir, exist_ok=True)
        
        # Generate chart filename
        chart_filename = f'progress_chart_{user_id}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.png'
        chart_path_absolute = os.path.join(graphs_dir, chart_filename)
        chart_path_relative = f"graphs/{chart_filename}"
        
        # Create comprehensive progress chart
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # BMI Chart
        ax1.plot(dates, bmi_values, marker='o', color='#06D6A0', linewidth=2, markersize=6)
        ax1.set_title('BMI Progress Over Time', fontsize=14, color='white', pad=20)
        ax1.set_xlabel('Date', fontsize=12, color='white')
        ax1.set_ylabel('BMI', fontsize=12, color='white')
        ax1.tick_params(colors='white')
        ax1.grid(True, alpha=0.3)
        
        # Volume Chart
        ax2.plot(dates, volumes, marker='s', color='#EF476F', linewidth=2, markersize=6)
        ax2.set_title('Workout Volume Over Time', fontsize=14, color='white', pad=20)
        ax2.set_xlabel('Date', fontsize=12, color='white')
        ax2.set_ylabel('Volume (sets × reps × weight)', fontsize=12, color='white')
        ax2.tick_params(colors='white')
        ax2.grid(True, alpha=0.3)
        
        # Rotate x-axis labels for better readability
        for ax in [ax1, ax2]:
            ax.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.gcf().set_facecolor('#2B1D41')
        
        # Save chart
        plt.savefig(chart_path_absolute, facecolor='#2B1D41', bbox_inches='tight', dpi=300)
        plt.close()
        
        chart_url = url_for('static', filename=chart_path_relative)
        
        return render_template('progress.html', 
                             user_id=user_id, 
                             chart_path=chart_url, 
                             has_data=True,
                             total_workouts=total_workouts,
                             avg_duration=round(avg_duration, 1),
                             total_volume=total_volume,
                             logs=logs[-10:])  # Show last 10 workouts
        
    except Exception as e:
        logger.error(f"Progress page error: {e}")
        flash('Error loading progress data.', 'error')
        return render_template('progress.html', user_id=user_id, has_data=False)

@app.route('/workout-history')
@login_required
def workout_history():
    user_id = session['user_id']
    
    try:
        page = int(request.args.get('page', 1))
        per_page = 10
        skip = (page - 1) * per_page
        
        # Get total count
        total_workouts = logs_col.count_documents({"user_id": user_id})
        total_pages = (total_workouts + per_page - 1) // per_page
        
        # Get paginated workouts
        workouts = list(logs_col.find({"user_id": user_id})
                       .sort("date", -1)
                       .skip(skip)
                       .limit(per_page))
        
        return render_template('workout_history.html', 
                             user_id=user_id,
                             workouts=workouts,
                             current_page=page,
                             total_pages=total_pages)
    
    except Exception as e:
        logger.error(f"Workout history error: {e}")
        flash('Error loading workout history.', 'error')
        return redirect(url_for('index'))

@app.route('/api/workout-stats')
@login_required
def workout_stats():
    user_id = session['user_id']
    
    try:
        # Get workout statistics
        total_workouts = logs_col.count_documents({"user_id": user_id})
        
        # Calculate streak
        workout_dates = [log['date'] for log in logs_col.find({"user_id": user_id}, {"date": 1})]
        streak = calculate_streak_days(workout_dates)
        
        # Get recent workouts
        recent_workouts = list(logs_col.find({"user_id": user_id})
                              .sort("date", -1)
                              .limit(5))
        
        return jsonify({
            'total_workouts': total_workouts,
            'streak': streak,
            'recent_workouts': recent_workouts
        })
    
    except Exception as e:
        logger.error(f"API error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)