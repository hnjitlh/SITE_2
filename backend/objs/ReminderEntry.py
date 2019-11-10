from app import db
from datetime import datetime


class ReminderEntry(db.Model):
    entry_id = db.column(db.Integer, primary_key=True)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.column(db.Integer, db.ForeignKey('message.msg_id'), nullable=True)
    time = db.column(db.DateTime)

    def get_message(self):
        pass

    def find_date_diff(self):
        return (datetime.utcnow() - self.time).days
