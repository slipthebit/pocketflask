#pocket/__init__.py
from flask import Flask

app = Flask(__name__)

import pocket.views