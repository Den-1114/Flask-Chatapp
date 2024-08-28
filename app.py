from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from flask_socketio import SocketIO 
from db_sctipt import *  # Ensure this is implemented correctly

app = Flask(__name__)

# Configurations
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = '@#$%^&123534GRFHGH'
socketio = SocketIO(app)

# Initialize session
Session(app)

# Home route
@app.route('/')
def hello_world():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


# Redirecting to the home route
@app.route('/index.html')
def index():
    return redirect('/')


# Route for chat page
@app.route('/chat.html')
def chat():
    if 'username' in session:
        return render_template('chat.html', ses="True", username=session['username'])
    else:
        return render_template('chat.html', ses="False")


@app.route('/room.html')
def room():
    return render_template('room.html')

# Login route
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            session['username'] = username
            return redirect('/chat.html')
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Register route
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            insert(username, password, email)
            return redirect('/login.html')
        else:
            return render_template('register.html', error="Passwords do not match")
    else:
        return render_template('register.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000) # Changed port to 5000 for local development
