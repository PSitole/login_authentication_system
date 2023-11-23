from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# User database (for demonstration purposes, use a database in a real application)
users = {}

# Route for the home page
@app.route('/')
def home():
    return 'Welcome to the Home Page!'

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if username in users:
            return 'Username already taken. Choose another one.'

        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='sha256')

        # Store the user information in the dictionary
        users[username] = {'username': username, 'password': hashed_password}

        return 'Registration successful. You can now <a href="/login">login</a>.'

    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists
        if username in users and check_password_hash(users[username]['password'], password):
            return f'Welcome, {username}! You have successfully logged in.'

        return 'Invalid username or password. <a href="/login">Try again</a>.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
