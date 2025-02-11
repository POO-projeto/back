from config import db


class ScholarShip(db.Model):
    __tablename__ = "scholarships"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
