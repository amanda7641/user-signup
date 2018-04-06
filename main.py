from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_index():
    return render_template('home.html', title = "User_Signup")

@app.route('/confirmation')
def confirm():
    username = request.args.get('username')
    return render_template('confirmation.html', title = "Confirmation", username = username)

@app.route('/', methods=['POST'])
def index():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    username_error = ''
    password_error = ''   
    verify_error = ''
    email_error = ''

    #see if username, password, or verify password are empty
    if (not username) or (username.strip() == ""):
        username_error = "Please enter a username."
    
    if (not password) or (password.strip() == ""):
        password_error = "Please enter a password."

    if (not verify_password) or (verify_password.strip() == ""):
        verify_error = "Please enter your password to verify."
    
    #if not are username and password the correct form
    if not username_error and not password_error and not verify_error and not email_error:
        if username.strip() != username or len(username)<3:
            username_error = "Your username cannot have spaces and must have 3+ characters."
        
        if password.strip() != password or len(password)<3:
            password_error = "Your password cannot have spaces and must have 3+ characters."
        
    #if not do the passwords match
    if not username_error and not password_error and not verify_error and not email_error:
        if password != verify_password:
            verify_error = "Your passwords do not match."
        
    #if not is the email okay
    if not username_error and not password_error and not verify_error and not email_error:
        if (email.strip() != "") and ((email.count("@")==1) or (email.count(".")==1) or (not (len(email)>3 and len(email)<20))):
            email_error = "Your email is not valid."

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect("/confirmation?username=" + username)
    else:
        #problem getting email to be valid
        return render_template('home.html', title = "User_Signup", 
        username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error, username=username, email=email)

app.run()