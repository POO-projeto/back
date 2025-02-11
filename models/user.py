from config import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    telephone = db.Column(db.String(13), nullable=True)
    github = db.Column(db.String(120), unique=True, nullable=True)
    lattes = db.Column(db.String(120), unique=True, nullable=True)
    scholarship_id = db.Column(
        db.Integer, db.ForeignKey("scholarships.id"), nullable=True
    )
    scholarship = db.relationship("ScholarShip", backref="user", lazy=True)
