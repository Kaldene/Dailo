from flask import Blueprint,render_template,request,redirect,url_for,flash
from models import User,db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user, logout_user
auth_routes = Blueprint('auth', __name__, url_prefix='/auth')

@auth_routes.route('/login',methods=['GET','POST'])
def login():
    return render_template("auth/login.html")






@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('auth_routes.login'))