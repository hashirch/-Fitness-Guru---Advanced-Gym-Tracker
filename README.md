# 💪 Fitness Guru

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.6+-yellow.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

A modern fitness tracking web application built with Flask and MongoDB. Track your workouts, monitor progress, and achieve your fitness goals.

## ✨ Features

- 🔐 **Secure Authentication** - Password hashing and session management
- 📊 **Workout Tracking** - Log exercises, sets, reps, and weights
- 📈 **Progress Charts** - Visualize your fitness journey
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🎯 **Smart Analytics** - BMI, BMR, TDEE calculations and health advice

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MongoDB

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fitness-guru.git
   cd fitness-guru
   ```

2. **Run setup script**
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

6. **Open browser**
   ```
   http://localhost:5000
   ```

## ⚙️ Configuration

Create a `.env` file:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
MONGO_URI=mongodb://localhost:27017/gym_tracker
```

## 📖 Usage

1. **Register** - Create your account
2. **Complete Profile** - Add your fitness information
3. **Log Workouts** - Track your exercises and progress
4. **View Progress** - Monitor your fitness journey

## 🛠️ Tech Stack

- **Backend**: Flask 3.0.0
- **Database**: MongoDB
- **Frontend**: Tailwind CSS, Font Awesome
- **Security**: Bcrypt, Werkzeug
- **Charts**: Matplotlib

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/register` | User registration |
| `POST` | `/login` | User authentication |
| `GET` | `/logout` | User logout |
| `GET` | `/profile` | View profile |
| `POST` | `/profile` | Update profile |
| `GET` | `/workout` | Workout form |
| `POST` | `/workout` | Log workout |
| `GET` | `/progress` | View progress charts |
| `GET` | `/workout-history` | View workout history |

## 🔒 Security

- Password hashing with bcrypt
- Input validation and sanitization
- Secure session management
- XSS and injection protection

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
```bash
# Check MongoDB status
sudo systemctl status mongod
```

**Import Errors**
```bash
# Activate virtual environment and reinstall
source venv/bin/activate
pip install -r requirements.txt
```

**Chart Generation Issues**
```bash
# Check directory permissions
chmod 755 static/graphs
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/fitness-guru/issues)
- **Documentation**: Check this README and inline code comments

---

<div align="center">

**Fitness Guru** - Your journey to a healthier you starts here! 💪

[![Star on GitHub](https://img.shields.io/github/stars/yourusername/fitness-guru?style=social)](https://github.com/yourusername/fitness-guru/stargazers)
[![Fork on GitHub](https://img.shields.io/github/forks/yourusername/fitness-guru?style=social)](https://github.com/yourusername/fitness-guru/network/members)

*Made with ❤️ by the Fitness Guru Team*

</div>
