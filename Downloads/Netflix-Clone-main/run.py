#!/usr/bin/env python3
"""
Simple script to run the Netflix clone website
"""
import os
import sys
import subprocess

def main():
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)

    # Check if requirements are installed
    try:
        import django
        print("✓ Django is installed")
    except ImportError:
        print("Installing requirements...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)

    # Run migrations if needed
    print("Running database migrations...")
    subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)

    # Collect static files
    print("Collecting static files...")
    subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], check=True)

    # Run the server
    print("\n🚀 Starting Netflix Clone server...")
    print("📱 Open your browser and go to: http://localhost:8000")
    print("❌ Press Ctrl+C to stop the server\n")

    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")

if __name__ == '__main__':
    main()