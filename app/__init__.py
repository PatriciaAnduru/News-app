from flask import Flask
from instance.config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting configuration
app.config.from_object(DevConfig)

from app import view


