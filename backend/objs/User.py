from app import db
from datetime import datetime
from .ReminderEntry import ReminderEntry


class User(db.Model):
    id = db.column(db.Integer, primary_key=True, nullable=False)
    name = db.column(db.String(80), nullable=False)
    register_time = db.column(db.Date, nullable=False, default=datetime.utcnow())

    def get_reminders(self):
        return ReminderEntry.query.filter_by(user_id=self.id).all()
