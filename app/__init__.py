from flask import Flask
from .config import config_options

# Initializing application
def create_app(config_name):
app = Flask(__name__)

# Setting up configuration
app.config.from_object(config_options[config_name])

