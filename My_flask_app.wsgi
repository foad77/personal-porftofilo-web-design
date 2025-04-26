#!/usr/bin/python3
import sys , os
import logging
from pathlib import Path
logging.basicConfig(stream=sys.stderr)

#sys.path.insert(0, "/home/Web/My_flask_app/")
sys.path.insert(0, Path(__file__).parent.resolve())

# Set the working directory to the app's directory
os.chdir(Path(__file__).parent.resolve())

from app import app as application  # Update this line to point to 'app.py'
