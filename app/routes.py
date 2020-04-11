from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Ketil'}
    return render_template('index.html', title='Home', user=user)

@app.route('/test')
def test():
    return "Heisann!"
