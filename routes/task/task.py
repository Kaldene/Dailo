from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required, current_user
from models.user import db
from models.task import Task

task_routes = Blueprint('task', __name__)

#задачи, поменять в base.html с дашборда и сделать отдельную функцию отвечающий за это

@task_routes.route('/task')
@login_required
def task():
    task = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template("task/task.html",task=task)



@task_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template("task/dashboard.html")


@task_routes.route('/create_task',methods=['GET','POST'])
@login_required
def create_task():
    return render_template("task/create_task.html")