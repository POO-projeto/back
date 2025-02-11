from config import db


class Daily(db.Model):
    __tablename__ = "dailies"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    issue = db.Column(db.String(100), default="Não", nullable=True)
    items = db.relationship("Item", backref="daily", lazy=True)
