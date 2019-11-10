from app import db


class Message(db.Model):
    msg_id = db.column(db.Integer, primary_key=True)
    text = db.column(db.TEXT, nullable=False)

    def value(self):
        return self.text
