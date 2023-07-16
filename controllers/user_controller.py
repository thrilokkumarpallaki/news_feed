from app.views import UserView


def register_user(**kwargs):
    name = kwargs.get('name')
    email = kwargs.get('email')
    password = kwargs.get('password')

    return UserView.register_user(name, email, password)


def login(**kwargs):
    email = kwargs.get('email')
    password = kwargs.get('password')

    return UserView.login(email, password)


def follow_user(**kwargs):
    user = kwargs.get('user')
    follower_id = kwargs.get('follower')

    return UserView.follow_user(user=user, follower_id=follower_id)
