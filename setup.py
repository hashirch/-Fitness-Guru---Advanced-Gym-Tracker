#!/usr/bin/env python3
"""
Setup script for Fitness Guru Gym Tracker
This script helps users set up the application quickly.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_banner():
    """Print the application banner"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    FITNESS GURU SETUP                        ║
    ║                                                              ║
    ║              Your journey to a healthier you starts here!    ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return
    
    print("📦 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        sys.exit(1)

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    
    # Determine the pip command based on OS
    if os.name == 'nt':  # Windows
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        pip_cmd = "venv/bin/pip"
    
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        print("Please run manually: pip install -r requirements.txt")
        sys.exit(1)

def create_env_file():
    """Create .env file from template"""
    env_file = Path(".env")
    env_example = Path("env_example.txt")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return
    
    if not env_example.exists():
        print("❌ env_example.txt not found")
        return
    
    print("📝 Creating .env file...")
    try:
        shutil.copy(env_example, env_file)
        print("✅ .env file created from template")
        print("⚠️  Please edit .env file with your configuration")
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")

def create_directories():
    """Create necessary directories"""
    directories = [
        "static/graphs",
        "static/uploads",
        "templates/errors"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Directories created")

def check_mongodb():
    """Check MongoDB connection"""
    print("🔍 Checking MongoDB connection...")
    try:
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        client.server_info()
        print("✅ MongoDB connection successful")
    except Exception as e:
        print("⚠️  MongoDB connection failed")
        print("   Please ensure MongoDB is running")
        print("   Or update MONGO_URI in .env file")

def print_next_steps():
    """Print next steps for the user"""
    print("""
    🎉 Setup completed successfully!
    
    Next steps:
    1. Edit .env file with your configuration
    2. Activate virtual environment:
       - Windows: venv\\Scripts\\activate
       - Unix/Mac: source venv/bin/activate
    3. Run the application:
       python app.py
    4. Open browser and go to: http://localhost:5000
    
    For more information, see README.md
    """)

def main():
    """Main setup function"""
    print_banner()
    
    print("🔍 Checking prerequisites...")
    check_python_version()
    
    print("\n📦 Setting up environment...")
    create_virtual_environment()
    install_requirements()
    
    print("\n📁 Creating directories...")
    create_directories()
    
    print("\n⚙️  Configuring application...")
    create_env_file()
    
    print("\n🔍 Checking database...")
    check_mongodb()
    
    print_next_steps()

if __name__ == "__main__":
    main() 