from models.user import User


def nest_user(obj):
    return User.query.get_or_404(obj.user_id)
