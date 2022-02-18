import os
from flask import Flask

app = Flask(__name__)
    
app.config['SECRET_KEY'] = "you can put anything"

from app import views