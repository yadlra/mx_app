from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/about')
# def about():
#     return '<h1>About page!</h1>'
