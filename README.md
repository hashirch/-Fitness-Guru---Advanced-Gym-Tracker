# 💪 Fitness Guru - Advanced Gym Tracker

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.6+-yellow.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> Your comprehensive fitness companion for tracking workouts, monitoring progress, and achieving your health goals.

Fitness Guru is a modern, secure, and feature-rich fitness tracking web application built with Flask and MongoDB. Whether you're a beginner starting your fitness journey or an experienced athlete tracking advanced metrics, Fitness Guru provides the tools you need to succeed.



> *Scre

## ✨ Key Features

### 🔐 **Secure Authentication**
- **Password Hashing**: Bcrypt encryption for maximum security
- **Email Validation**: Proper email format verification
- **Session Management**: Secure session handling with HTTP-only cookies
- **Input Sanitization**: Protection against XSS and injection attacks

### 📊 **Comprehensive Tracking**
- **Workout Logging**: Track exercises, sets, reps, weights, and difficulty
- **Progress Visualization**: Beautiful charts showing BMI and volume trends
- **Real-time Calculations**: Instant volume, one-rep max, and duration calculations
- **Workout History**: Paginated view with detailed workout information

### 🎯 **Smart Analytics**
- **BMI Tracking**: Automatic BMI calculation and health category classification
- **BMR & TDEE**: Basal Metabolic Rate and Total Daily Energy Expenditure
- **Health Advice**: Personalized recommendations based on your metrics
- **Streak Tracking**: Monitor your consistency and build healthy habits

### 📱 **Modern User Experience**
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Dark Theme**: Easy on the eyes with beautiful dark color scheme
- **Interactive Forms**: Real-time validation and instant feedback
- **Flash Messages**: Auto-dismissing notifications for user feedback

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend Framework** | Flask | 3.0.0 |
| **Database** | MongoDB | 4.6+ |
| **Frontend** | Tailwind CSS | Latest |
| **Icons** | Font Awesome | 6.0+ |
| **Charts** | Matplotlib | 3.8.2 |
| **Security** | Bcrypt | 4.1.2 |
| **Configuration** | Python-dotenv | 1.0.0 |

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **MongoDB** - [Install MongoDB](https://docs.mongodb.com/manual/installation/)
- **Git** - [Install Git](https://git-scm.com/downloads)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fitness-guru.git
   cd fitness-guru
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Configure environment**
   ```bash
   # Edit .env file with your settings
   nano .env
   ```

5. **Start the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   ```
   http://localhost:5000
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your-super-secret-key-here

# Database Configuration
MONGO_URI=mongodb://localhost:27017/gym_tracker

# Security Settings
SESSION_COOKIE_SECURE=False

# Email Configuration (for future features)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### Database Setup

The application supports both local and cloud MongoDB:

- **Local MongoDB**: `mongodb://localhost:27017/gym_tracker`
- **MongoDB Atlas**: `mongodb+srv://username:password@cluster.mongodb.net/gym_tracker`

## 📖 User Guide

### Getting Started

1. **Create Account**: Register with username, email, and secure password
2. **Complete Profile**: Add your age, gender, height, weight, and fitness goals
3. **Log First Workout**: Start tracking your exercises and progress
4. **Monitor Progress**: View charts and statistics to track improvement

### Features Overview

#### 🔐 Authentication
- Secure registration with email validation
- Password strength requirements
- Remember me functionality
- Secure logout

#### 👤 Profile Management
- Personal information storage
- Fitness goal setting
- Activity level selection
- Automatic health calculations

#### 💪 Workout Logging
- Exercise name and duration
- Sets, reps, and weight tracking
- Difficulty rating system
- Optional notes and comments
- Real-time calculations

#### 📈 Progress Tracking
- BMI progress visualization
- Workout volume trends
- Performance statistics
- Health recommendations

#### 📚 Workout History
- Complete workout log
- Detailed exercise information
- Performance metrics
- Search and filter (coming soon)

## 🔒 Security Features

### Password Security
- **Minimum Requirements**: 6+ characters
- **Hashing**: Bcrypt with salt
- **Strength Indicators**: Real-time password strength feedback
- **Secure Verification**: Safe password comparison

### Data Protection
- **Input Validation**: Comprehensive form validation
- **XSS Prevention**: Input sanitization
- **SQL Injection Protection**: Parameterized queries
- **Session Security**: HTTP-only, secure cookies

### Privacy
- **User Data Isolation**: Each user's data is completely separate
- **No Data Sharing**: Your information stays private
- **Secure Storage**: Encrypted sensitive data

## 🎨 User Interface

### Design Philosophy
- **Modern Aesthetic**: Clean, professional design
- **Dark Theme**: Reduced eye strain for extended use
- **Consistent Branding**: Unified color scheme and typography
- **Accessibility**: Keyboard navigation and screen reader support

### Responsive Design
- **Mobile-First**: Optimized for smartphone use
- **Tablet Support**: Enhanced experience on tablets
- **Desktop Optimization**: Full-featured desktop interface
- **Touch-Friendly**: Large touch targets for mobile devices

## 📊 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/register` | User registration |
| `POST` | `/login` | User authentication |
| `GET` | `/logout` | User logout |

### Profile Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/profile` | View user profile |
| `POST` | `/profile` | Update profile information |

### Workout Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/workout` | Workout logging form |
| `POST` | `/workout` | Log new workout |
| `GET` | `/workout-history` | View workout history |
| `GET` | `/progress` | View progress charts |

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/workout-stats` | Get workout statistics |

## 🚀 Deployment

### Local Development
```bash
# Development mode
export FLASK_ENV=development
python app.py
```

### Production Deployment

1. **Set production environment**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-production-secret-key
   ```

2. **Use production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Set up reverse proxy (Nginx)**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Error
```bash
# Check MongoDB status
sudo systemctl status mongod

# Restart MongoDB
sudo systemctl restart mongod

# Verify connection string in .env
MONGO_URI=mongodb://localhost:27017/gym_tracker
```

#### Import Errors
```bash
# Activate virtual environment
source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt
```

#### Chart Generation Issues
```bash
# Check directory permissions
chmod 755 static/graphs

# Verify matplotlib backend
echo "import matplotlib; print(matplotlib.get_backend())"
```

#### Session Issues
```bash
# Verify SECRET_KEY in .env
SECRET_KEY=your-secret-key-here

# Clear browser cookies
# Check browser cookie settings
```

### Debug Mode
```bash
# Enable debug mode
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/fitness-guru.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add tests for new features
   - Update documentation

4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

### Development Guidelines

- **Code Style**: Follow PEP 8 guidelines
- **Testing**: Add tests for new features
- **Documentation**: Update README and docstrings
- **Security**: Follow security best practices
- **Performance**: Optimize for speed and efficiency

## 📋 Roadmap

### 🎯 Upcoming Features

- [ ] **Social Features**: Friend connections and workout sharing
- [ ] **Advanced Analytics**: Detailed progress insights and predictions
- [ ] **Workout Templates**: Pre-defined workout routines
- [ ] **Goal Setting**: SMART goal tracking and reminders
- [ ] **Notifications**: Email and push notifications
- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Data Export**: Export data in CSV, JSON, and PDF formats
- [ ] **Integration**: Connect with fitness devices and apps

### 🔧 Technical Improvements

- [ ] **Caching**: Redis integration for better performance
- [ ] **Background Jobs**: Celery for async task processing
- [ ] **Testing**: Comprehensive test suite with 90%+ coverage
- [ ] **CI/CD**: Automated deployment pipeline
- [ ] **Monitoring**: Application monitoring and logging
- [ ] **API**: RESTful API for third-party integrations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Fitness Guru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **Flask Community** - For the excellent web framework and documentation
- **Tailwind CSS** - For the beautiful and responsive styling system
- **MongoDB** - For the flexible and scalable database solution
- **Font Awesome** - For the comprehensive icon library
- **Matplotlib** - For the powerful charting capabilities
- **Bcrypt** - For the secure password hashing implementation

## 📞 Support

### Getting Help

- **Documentation**: Check this README and inline code comments
- **Issues**: Create an issue in the GitHub repository
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Wiki**: Check the project wiki for detailed guides

### Community

- **GitHub Issues**: [Report bugs and request features](https://github.com/yourusername/fitness-guru/issues)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/yourusername/fitness-guru/discussions)
- **Contributing**: [Help improve the project](https://github.com/yourusername/fitness-guru/blob/main/CONTRIBUTING.md)

### Contact

- **Email**: support@fitnessguru.com
- **Twitter**: [@FitnessGuruApp](https://twitter.com/FitnessGuruApp)
- **Discord**: [Join our community](https://discord.gg/fitnessguru)

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/yourusername/fitness-guru)
![GitHub forks](https://img.shields.io/github/forks/yourusername/fitness-guru)
![GitHub issues](https://img.shields.io/github/issues/yourusername/fitness-guru)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/fitness-guru)
![GitHub contributors](https://img.shields.io/github/contributors/yourusername/fitness-guru)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/fitness-guru)

---

<div align="center">

**Fitness Guru** - Your journey to a healthier you starts here! 💪

[![Star on GitHub](https://img.shields.io/github/stars/yourusername/fitness-guru?style=social)](https://github.com/yourusername/fitness-guru/stargazers)
[![Fork on GitHub](https://img.shields.io/github/forks/yourusername/fitness-guru?style=social)](https://github.com/yourusername/fitness-guru/network/members)
[![Watch on GitHub](https://img.shields.io/github/watchers/yourusername/fitness-guru?style=social)](https://github.com/yourusername/fitness-guru/watchers)

*Made with ❤️ by the Fitness Guru Team*

</div> #   - F i t n e s s - G u r u - - - A d v a n c e d - G y m - T r a c k e r  
 