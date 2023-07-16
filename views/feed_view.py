from app.helpers import print_human_understandable_time
from app.models import CommentModel, FeedModel, UserModel
from app.expcetions import FeedObjectDoesNotExistException, UserDoesNotExistException, CommentObjectCreationException, \
    FeedObjectCreationException


class FeedView:
    @staticmethod
    def create_post(**kwargs):
        """
        This method creates a feed entry.
        :param kwargs:
        :return:
        """
        user = kwargs.get('user')
        content = kwargs.get('content')

        # check if user is a valid user or not
        is_present = UserModel.is_user_present(user)
        if not is_present:
            raise UserDoesNotExistException("Invalid user id!")

        feed_obj = FeedModel(user=user, content=content)
        feed_status = feed_obj.save()

        if not feed_status:
            raise FeedObjectCreationException('Something went wrong while creating Feed!')

        return 'SUCCESS'

    @staticmethod
    def create_comment(**kwargs):
        feed = kwargs.get('feed')
        user = kwargs.get('user')
        comment = kwargs.get('comment')
        comment_id = kwargs.get('comment_id', None)

        # Check if the user is a valid user or not
        is_present = UserModel.is_user_present(user)
        if not is_present:
            raise UserDoesNotExistException('Invalid user id!')

        # Check if the feed obj is a valid feed or not
        is_feed_present = FeedModel.is_feed_present(feed)
        if not is_feed_present:
            raise FeedObjectDoesNotExistException('Invalid feed id!')

        comment_obj = CommentModel(feed=feed, user=user, comment=comment, comment_id=comment_id)
        comment_status = comment_obj.save()

        if not comment_status:
            raise CommentObjectCreationException('Something went wrong while creating comment!')
        return 'SUCCESS'

    @staticmethod
    def upvote_feed(**kwargs) -> str:
        feed = kwargs.get('feed')
        user = kwargs.get('user')

        # Check if the user is a valid user or not
        is_present = UserModel.is_user_present(user)
        if not is_present:
            raise UserDoesNotExistException('Invalid user id!')

        # upvote the feed
        upvote_status = FeedModel.upvote_feed(feed)
        if not upvote_status:
            return 'FAILED'
        return 'SUCCESS'

    @staticmethod
    def downvote_feed(**kwargs) -> str:
        feed = kwargs.get('feed')
        user = kwargs.get('user')

        # Check if the user is a valid user or not
        is_present = UserModel.is_user_present(user)
        if not is_present:
            raise UserDoesNotExistException('Invalid user id!')

        # Downvote the feed
        downvote_status = FeedModel.downvote_feed(feed)
        if not downvote_status:
            return 'FAILED'
        return 'SUCCESS'

    @staticmethod
    def show_newsfeed(**kwargs):
        user = int(kwargs.get('user', 0))

        # Get news feed
        news_feed = FeedModel.get_newsfeed(user)
        for feed in news_feed:
            created_at = print_human_understandable_time(feed.created_at)
            print(feed.id, feed.content, created_at)

    @staticmethod
    def upvote_comment(**kwargs) -> str:
        comment = kwargs.get('comment')
        user = kwargs.get('user')

        # Check if the user is a valid user or not
        is_present = UserModel.is_user_present(user)
        if not is_present:
            raise UserDoesNotExistException('Invalid user id!')

        # upvote the feed
        upvote_status = CommentModel.upvote_comment(comment)
        if not upvote_status:
            return 'FAILED'
        return 'SUCCESS'

    @staticmethod
    def downvote_comment(**kwargs) -> str:
        feed = kwargs.get('comment')
        user = kwargs.get('user')

        # Check if the user is a valid user or not
        is_present = UserModel.is_user_present(user)
        if not is_present:
            raise UserDoesNotExistException('Invalid user id!')

        # Downvote the feed
        downvote_status = CommentModel.downvote_comment(feed)
        if not downvote_status:
            return 'FAILED'
        return 'SUCCESS'
