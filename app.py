from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to Web-App !</h1>'

@app.route('/about')
def about():
    return '<h3>This is the About Page of the Web-App</h3>'

if __name__ == '__main__':
    app.run(debug=True)
