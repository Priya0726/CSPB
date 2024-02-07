from flask import Flask, render_template, request, redirect, url_for
from flask_sass import Sass

app = Flask(__name__)
sass = Sass(app)

# A simple list to store usernames and passwords (for educational purposes only)
user_credentials = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # Check if the entered credentials match the stored credentials
    if username in user_credentials and user_credentials[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid credentials. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
