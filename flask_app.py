from flask import Flask, flash, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return hello_world()

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return hello_world()



@app.route('/')
def hello_world():
    return """

<b>
hallo iedereen!
<b>

<a href="https://alexd31.pythonanywhere.com">Naar Alex</a><br>
<a href="https://kearon.pythonanywhere.com">Naar Kearon</a>



<body style="background-color:powderblue;">

<h1>My First JavaScript</h1>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

<p id="demo"></p>


"""



