import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'secret-key-lesson35'
    # მონაცემთა ბაზა: lesson35_hw.db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'lesson35_hw.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False