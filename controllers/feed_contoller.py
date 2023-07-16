from app.views import FeedView


def create_post(user, content):
    return FeedView.create_post(user=user, content=content)


def create_comment(feed, user, comment, comment_id):
    return FeedView.create_comment(feed=feed, user=user, comment=comment, comment_id=comment_id)


def upvote_feed(feed, user):
    return FeedView.upvote_feed(feed=feed, user=user)


def downvote_feed(feed, user):
    return FeedView.downvote_feed(feed=feed, user=user)


def show_newsfeed(user):
    return FeedView.show_newsfeed(user=user)


def upvote_comment(comment, user):
    return FeedView.upvote_comment(comment=comment, user=user)


def downvote_comment(comment, user):
    return FeedView.downvote_comment(comment=comment, user=user)
