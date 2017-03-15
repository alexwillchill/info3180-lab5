"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db #login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm, UserProfile
from app.models import UserProfile
from werkzeug.utils import secure_filename
import time
import uuid
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###
@app.route('/profile/', methods=["GET","POST"])
def addProfile():
    #Adds new user profile
    form= UserProfile()
    if request== "POST":
        if form.validate_on_submit:
        
            userid= str(uuid.uuid4())
            firstname= request.form['firstname']
            lastname=request.form['lastname']
            username=request.form['username']
            age=request.form['age']
            biography=request.form['biography']
            gender= request.form["gender"]
            image=form.image.data
            
            file_folder= app.config['UPLOAD_FOLDER']
            filename= secure_filename(image.filename)
            image.save(os.path.join(file_folder, filename))
            entry_date = time.strftime("%a %d %B %Y")

            user= UserProfile(userid=userid,firstname=firstname,lastname=lastname,age=age,biography=biography,username=username)
            db.session.add(user)
            db.session.commit()
            
            flash("New user created")
    return render_template('newprofile.html')   
    
    
@app.route("/profiles",methods=["GET","POST"])
def viewProfile():
    return render_template('profile.html')
    
@app.route("/profiles/<userid>",methods=["GET","POST"])
def listProfiles():
    return render_template('profilelist.html')
    
    
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for("home"))
    form= LoginForm()# change this to actually validate the entire form submission
        # and not just one field
    if form.username.data:
        username=form.username.data
        password=form.password.data
        
            # Get the username and password values from the form.

            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.
        user=UserProfile.query.filter_by(username=username,password=password).first()
            # get user id, load into session
        if user is not None:
            login_user(user)
        
            # remember to flash a message to the user
            
            
            # they should be redirected to a secure-page route instead
            flash("Welcome login was a sucess","sucess")
            return redirect(url_for("secure-page"))
        else:
            flash("Username or password entered wrong","danger")
    flash_error(forms)
    return render_template("login.html", form=form)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        
        flash('You have been logged out', 'warning')
        logout_user()
        return redirect(url_for("home"))
    
    return redirect(url_for("home"))
    
    
    
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
    
    
    
#The routes down here 
#@app.form('/form.txt/')