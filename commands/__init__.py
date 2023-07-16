import click
from flask.cli import with_appcontext

from app.controllers import user_controller, feed_contoller


@click.command(name='login')
@click.option('--username')
@click.password_option('--password')
@with_appcontext
def user_login(username, password):
    user = user_controller.login(email=username, password=password)
    print(user)


@click.command(name='signup')
@click.option('--name')
@click.option('--email')
@click.password_option('--password')
def user_signup(name, email, password):
    status = user_controller.register_user(name=name, email=email, password=password)
    print(status)


@click.command(name='post')
@click.option('--user')
@click.option('--content')
def post_feed(user, content):
    status = feed_contoller.create_post(user=user, content=content)
    print(status)


@click.command(name='follow')
@click.option('--user')
@click.option('--follower')
def follow_user(user, follower):
    status = user_controller.follow_user(user=user, follower=follower)
    print(status)


@click.command(name='reply')
@click.option('--user')
@click.option('--feed')
@click.option('--comment')
@click.option('--comment_id')
def post_comment(user, feed, comment, comment_id=None):
    status = feed_contoller.create_comment(feed=feed, user=user, comment=comment, comment_id=comment_id)
    print(status)


@click.command(name='upvote-feed')
@click.option('--user')
@click.option('--feed')
def upvote_feed(user, feed):
    status = feed_contoller.upvote_feed(user=user, feed=feed)
    print(status)


@click.command(name='downvote-feed')
@click.option('--user')
@click.option('--feed')
def downvote_feed(user, feed):
    status = feed_contoller.downvote_feed(user=user, feed=feed)
    print(status)


@click.command(name='upvote-comment')
@click.option('--user')
@click.option('--comment')
def upvote_comment(user, comment):
    status = feed_contoller.upvote_comment(user=user, comment=comment)
    print(status)


@click.command(name='downvote-comment')
@click.option('--user')
@click.option('--comment')
def downvote_comment(user, comment):
    status = feed_contoller.downvote_comment(user=user, comment=comment)
    print(status)


@click.command(name='newsfeed')
@click.option('--user')
def show_newsfeed(user):
    newsfeed = feed_contoller.show_newsfeed(user=user)
