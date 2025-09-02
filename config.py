# Configuration file for the service
import os
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

class Config:
    """Application's base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
