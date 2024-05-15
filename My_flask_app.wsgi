#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/Web/My_flask_app/")

from app import app as application  # Update this line to point to 'app.py'
