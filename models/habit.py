from . import db
from datetime import datetime

#на доработке
class Habit(db.Model):
    __tablename__ = 'habit'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    due_date = db.Column(db.Date, nullable=True)
    due_time = db.Column(db.Time, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'