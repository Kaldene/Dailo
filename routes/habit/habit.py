from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required, current_user
from models import db
from datetime import datetime

habit_routes = Blueprint('habit',__name__)

#Список привычек
@habit_routes.route('/habit')
@login_required
def habit():
    return render_template('habit.html')

@habit_routes.route('/habit_create',methods=['GET','POST'])
@login_required
def habit_create():
    if request.method == 'GET':
        return render_template('habit_create.html')