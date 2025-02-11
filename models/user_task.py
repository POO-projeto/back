from config import db


class UserTask(db.Model):
    __tablename__ = "user_tasks"
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
