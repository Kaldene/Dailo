import os


class Config:
    SECRET_KEY = 'super-secret-key-for-dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEATHER_API_KEY = 'c4d582805f2e493e8f2210452260404'