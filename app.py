from flask import Flask, render_template, request, redirect, url_for, flash

application = Flask(__name__)
application.secret_key = 'your_secret_key'

USERNAME = "reetika"
PASSWORD = "gadhi"

@application.route('/')
def login():
    return render_template('login.html')

@application.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('home'))
    else:
        flash("Invalid credentials. Please try again.")
        return redirect(url_for('login'))

@application.route('/home')
def home():
    return render_template('index.html')
