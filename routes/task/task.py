from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required, current_user
from models.task import Task
from models import db
from datetime import datetime

task_routes = Blueprint('task', __name__)


@task_routes.route('/task')
@login_required
def task():
    task = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template("task/task.html",task=task)

@task_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template("main/dashboard.html")


#работает
@task_routes.route('/create_task',methods=['GET','POST'])
@login_required
def create_task():
    if request.method == 'GET':
        return render_template("task/create_task.html")

    if request.method == 'POST':
        #получаем данные из формы
        title = request.form.get('title', "").strip()
        description = request.form.get('description', "").strip() or None
        priority = request.form.get('priority', 'low')
        category = request.form.get('category') or None
        due_date_str = request.form.get('due_date')
        due_time_str = request.form.get('due_time')

        #валидация обязательных полей
        if not title:
            flash('Название задачи обязательно!', 'error')
            return redirect(url_for('task.create_task'))

        if len(title) > 200:
            flash('Название слишком длинное (макс. 200 символов)', 'error')
            return redirect(url_for('task.create_task'))

        due_date = None
        due_time = None

        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Неверный формат даты', 'error')
                return redirect(url_for('task.create_task'))

        if due_time_str:
            try:
                due_time = datetime.strptime(due_time_str, '%H:%M').time()
            except ValueError:
                flash('Неверный формат времени', 'error')
                return redirect(url_for('task.create_task'))

        #создание новой задачи
        new_task = Task(
            title=title,
            description=description,
            priority=priority,
            category=category,
            due_date=due_date,
            due_time=due_time,
            user_id=current_user.id
        )

        try:
            db.session.add(new_task)
            db.session.commit()
            flash('Задача успешно создана!', 'success')
            return redirect(url_for('task.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f' Ошибка при сохранении:', 'error')
            return redirect(url_for('task.create_task'))

