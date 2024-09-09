from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Welcome to Web-App !</h1>'

@app.route('/about/')
def about():
    return '<h3>This is the About Page of the Web-App</h3>'