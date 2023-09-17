from musicPackage import app
from flask import render_template, url_for, redirect, flash, get_flashed_messages, request
from musicPackage.models import User
from musicPackage import db
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/LaMusic")
def home():
    return render_template('index.html')


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_address = request.form.get('email')
        password = request.form.get('password')
        # global email
        # global password
        # email = email_address
        # password = passowrd_address
        getting_user_email = User.query.filter_by(email=email_address).first()
        getting_user_password = User.query.filter_by(password=password).first()
        # user = getting_user_email.email
        if getting_user_email is not None and getting_user_email.email is not None:# and getting_user_password.password is not None:
            if email_address == getting_user_email.email: 
                if bcrypt.check_password_hash(getting_user_email.password, password):
                    flash('You were successfully logged in!','success')
                    print('error in pass1')
                    return redirect(url_for('home'))
                else:
                    flash(f'Password Is Wrong!', 'password_error')
                    print('error in pass2')
                    return render_template('login.html')
            else:
                flash('This email is incorrect!','wrong_email')
                return render_template('login.html')
        else:
            flash(f'This email does not exists!', 'email_error')
            print('error in email')
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # hash_password = bcrypt.generate_password_hash(passowrd).decode('utf-8')
    # new_user = User(email=email_address, password=hash_password)
    # db.session.add(new_user)
    # db.session.commit()
    if request.method == "POST":
        fname = request.form['first_name']
        lname = request.form['last_name']
        username = request.form['username']
        email = request.form['email_address']
        password_ = request.form['password']
        hash_password = bcrypt.generate_password_hash(password_).decode('utf-8')
        new_user0 = User(fname=fname,lname=lname,username=username,email=email,password=hash_password)
        db.session.add(new_user0)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@app.route("/logged")
def logged():
    return f'Your email is #email and your pass is #password'