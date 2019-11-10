from app import db


class User(db.Model):
    id = db.column(db.Integer, primary_key=True, nullable=False)
    name = db.column(db.String(80), nullable=False)

    def get_reminders(self):
        pass
