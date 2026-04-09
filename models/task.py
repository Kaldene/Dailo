from . import db
from datetime import datetime, timezone

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    priority = db.Column(db.String(10), default='low', nullable=False)  # low, medium, high
    category = db.Column(db.String(50), nullable=True)  # work, personal, health, study
    due_date = db.Column(db.Date, nullable=True)  # Для <input type="date">
    due_time = db.Column(db.Time, nullable=True)  # Для <input type="time">

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'