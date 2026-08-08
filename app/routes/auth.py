from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            session['user'] = user.username
            flash('Login successful', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('Logged out','info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash("Username already exists", 'error')
            return redirect(url_for('auth.register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.", 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

