import click

from .commands import Command
from app.controllers import user_controller, feed_contoller


@click.command(name=Command.LOGIN)
@click.option('--username')
@click.password_option('--password')
def user_login(username, password):
    user = user_controller.login(email=username, password=password)
    print(user)


@click.command(name=Command.SIGNUP)
@click.option('--name')
@click.option('--email')
@click.password_option('--password')
def user_signup(name, email, password):
    status = user_controller.register_user(name=name, email=email, password=password)
    print(status)


@click.command(name=Command.POST)
@click.option('--user')
@click.option('--content')
def post_feed(user, content):
    status = feed_contoller.create_post(user=user, content=content)
    print(status)


@click.command(name=Command.FOLLOW)
@click.option('--user')
@click.option('--follower')
def follow_user(user, follower):
    status = user_controller.follow_user(user=user, follower=follower)
    print(status)


@click.command(name=Command.REPLY)
@click.option('--user')
@click.option('--feed')
@click.option('--comment')
@click.option('--comment_id')
def post_comment(user, feed, comment, comment_id=None):
    status = feed_contoller.create_comment(feed=feed, user=user, comment=comment, comment_id=comment_id)
    print(status)


@click.command(name=Command.UPVOTE_FEED)
@click.option('--user')
@click.option('--feed')
def upvote_feed(user, feed):
    status = feed_contoller.upvote_feed(user=user, feed=feed)
    print(status)


@click.command(name=Command.DOWNVOTE_FEED)
@click.option('--user')
@click.option('--feed')
def downvote_feed(user, feed):
    status = feed_contoller.downvote_feed(user=user, feed=feed)
    print(status)


@click.command(name=Command.UPVOTE_COMMENT)
@click.option('--user')
@click.option('--comment')
def upvote_comment(user, comment):
    status = feed_contoller.upvote_comment(user=user, comment=comment)
    print(status)


@click.command(name=Command.DOWNVOTE_COMMENT)
@click.option('--user')
@click.option('--comment')
def downvote_comment(user, comment):
    status = feed_contoller.downvote_comment(user=user, comment=comment)
    print(status)


@click.command(name=Command.NEWS_FEED)
@click.option('--user')
def show_newsfeed(user):
    newsfeed = feed_contoller.show_newsfeed(user=user)
