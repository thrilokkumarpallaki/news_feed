import os

from flask import Flask

from db_connect import redis_client

application = Flask(__name__)

from app.commands import *
from expcetions import register_exceptions


application.cli.add_command(user_login)
application.cli.add_command(user_signup)
application.cli.add_command(post_feed)
application.cli.add_command(follow_user)
application.cli.add_command(post_comment)
application.cli.add_command(upvote_feed)
application.cli.add_command(downvote_feed)
application.cli.add_command(upvote_comment)
application.cli.add_command(downvote_comment)
application.cli.add_command(show_newsfeed)
