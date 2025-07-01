import re
import bcrypt
from datetime import datetime, timedelta
import math

def calculate_bmi(weight, height):
    """Calculate BMI with validation"""
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values")
    return round(weight / ((height / 100) ** 2), 2)

def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation"""
    if weight <= 0 or height <= 0 or age <= 0:
        raise ValueError("Weight, height, and age must be positive values")
    
    if gender.lower() == 'male':
        return round(10 * weight + 6.25 * height - 5 * age + 5, 2)
    elif gender.lower() == 'female':
        return round(10 * weight + 6.25 * height - 5 * age - 161, 2)
    else:
        raise ValueError("Gender must be 'male' or 'female'")

def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure"""
    activity_multipliers = {
        'sedentary': 1.2,      # Little or no exercise
        'light': 1.375,        # Light exercise 1-3 days/week
        'moderate': 1.55,      # Moderate exercise 3-5 days/week
        'active': 1.725,       # Hard exercise 6-7 days/week
        'very_active': 1.9     # Very hard exercise, physical job
    }
    
    if activity_level not in activity_multipliers:
        raise ValueError("Invalid activity level")
    
    return round(bmr * activity_multipliers[activity_level], 2)

def get_bmi_category(bmi):
    """Get BMI category and health implications"""
    if bmi < 18.5:
        return "Underweight", "Consider gaining weight through healthy diet and exercise"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "Maintain your healthy weight"
    elif 25 <= bmi < 30:
        return "Overweight", "Consider weight loss through diet and exercise"
    else:
        return "Obese", "Consult a healthcare provider for weight management"

def hash_password(password):
    """Hash password using bcrypt"""
    if not password or len(password) < 6:
        raise ValueError("Password must be at least 6 characters long")
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_username(username):
    """Validate username format"""
    if not username or len(username) < 3:
        return False, "Username must be at least 3 characters long"
    if len(username) > 20:
        return False, "Username must be less than 20 characters"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    return True, "Username is valid"

def calculate_workout_volume(sets, reps, weight=None):
    """Calculate workout volume (sets * reps * weight)"""
    volume = sets * reps
    if weight:
        volume *= weight
    return volume

def calculate_one_rep_max(weight, reps):
    """Calculate estimated one-rep max using Epley formula"""
    if reps == 1:
        return weight
    return round(weight * (1 + reps / 30), 2)

def format_duration(minutes):
    """Format duration in a human-readable way"""
    if minutes < 60:
        return f"{minutes} minutes"
    hours = minutes // 60
    remaining_minutes = minutes % 60
    if remaining_minutes == 0:
        return f"{hours} hour{'s' if hours != 1 else ''}"
    return f"{hours} hour{'s' if hours != 1 else ''} {remaining_minutes} minutes"

def get_workout_difficulty_rating(difficulty):
    """Convert numeric difficulty to descriptive rating"""
    difficulty_map = {
        1: "Very Easy",
        2: "Easy", 
        3: "Moderate",
        4: "Hard",
        5: "Very Hard"
    }
    return difficulty_map.get(difficulty, "Unknown")

def calculate_streak_days(workout_dates):
    """Calculate current workout streak"""
    if not workout_dates:
        return 0
    
    # Sort dates in descending order
    sorted_dates = sorted(workout_dates, reverse=True)
    today = datetime.now().date()
    
    streak = 0
    current_date = today
    
    for date_str in sorted_dates:
        if isinstance(date_str, str):
            workout_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            workout_date = date_str
            
        if current_date == workout_date:
            streak += 1
            current_date -= timedelta(days=1)
        elif current_date > workout_date:
            break
    
    return streak

def sanitize_input(text):
    """Basic input sanitization"""
    if not text:
        return ""
    # Remove potentially dangerous characters
    return re.sub(r'[<>"\']', '', str(text).strip())

def validate_workout_data(workout, duration, reps, sets, difficulty):
    """Validate workout form data"""
    errors = []
    
    if not workout or len(workout.strip()) < 2:
        errors.append("Workout name must be at least 2 characters long")
    
    if not isinstance(duration, int) or duration < 1 or duration > 480:
        errors.append("Duration must be between 1 and 480 minutes")
    
    if not isinstance(reps, int) or reps < 1 or reps > 1000:
        errors.append("Reps must be between 1 and 1000")
    
    if not isinstance(sets, int) or sets < 1 or sets > 50:
        errors.append("Sets must be between 1 and 50")
    
    if not isinstance(difficulty, int) or difficulty < 1 or difficulty > 5:
        errors.append("Difficulty must be between 1 and 5")
    
    return errors
