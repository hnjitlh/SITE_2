from app import db
from datetime import datetime
from .Messages import Message


class ReminderEntry(db.Model):
    entry_id = db.column(db.Integer, primary_key=True)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.column(db.Integer, db.ForeignKey('message.msg_id'), nullable=True)
    time = db.column(db.DateTime)

    def get_message(self):
        return Message.query.filter_by(msg_id=self.message).first()

    def find_date_diff(self):
        return (datetime.utcnow() - self.time).days
