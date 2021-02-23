from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return 'This is a Simple Hello'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('Flask_Demo.html', name=name)
