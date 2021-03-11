# pocket/views.py
from pocket import app
from flask import render_template

@app.route('/')
def hello_world():
    return 'Say hello to your little PocketFlask'

@app.route('/pocket')
def pocket(name=None):
    return render_template('maintemplate.html', name=name)