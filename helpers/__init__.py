from datetime import datetime
from pytz import timezone

from flask_bcrypt import generate_password_hash, check_password_hash

tz = timezone('America/Denver')


def encrypt_password(plain_password: str) -> str:
    pass_hash = generate_password_hash(password=plain_password, rounds=10).decode('utf-8')
    return pass_hash


def validate_password(pass_hash: str, user_password: str) -> bool:
    return check_password_hash(pass_hash, user_password)


def print_human_understandable_time(post_dt: datetime):
    current_dt = datetime.now(tz=tz)
    delta = current_dt - post_dt

    hours, reminder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(reminder, 60)

    if hours != 0 and hours < 24:
        return f'{hours} hours ago'
    elif minutes != 0:
        return f'{minutes} minutes ago'
    else:
        return 'Just Now'
