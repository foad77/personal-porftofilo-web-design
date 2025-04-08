#!/usr/bin/python3
import sys , os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/Web/My_flask_app/")

# Set the working directory to the app's directory
os.chdir("/home/Web/My_flask_app/")

from app import app as application  # Update this line to point to 'app.py'
