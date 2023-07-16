from . import *
from .comment_model import CommentModel
from .user_follower_mapping_model import FollowerModel
from .user_model import UserModel
from app.expcetions import FeedObjectDoesNotExistException, UserDoesNotExistException


class FeedModel(Base):
    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(TEXT, nullable=False)
    upvote = Column(Integer, default=0)
    downvote = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    last_modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def save(self):
        session = Session(expire_on_commit=True)
        status = False
        try:
            session.add(self)
            session.commit()
            status = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status

    @staticmethod
    def is_feed_present(feed_id: int):
        session = Session()
        is_present = False
        try:
            feed_count = session.query(FeedModel.id == feed_id).count()
            if feed_count == 1:
                is_present = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return is_present

    @staticmethod
    def upvote_feed(feed_id: int):
        session = Session(expire_on_commit=True)
        session.connection(execution_options={'isolation_level': 'SERIALIZABLE'})
        status = False
        try:
            feed_obj = session.query(FeedModel).filter(FeedModel.id == feed_id).first()

            if feed_obj is not None:
                feed_obj.upvote += 1
                session.commit()
                status = True
            else:
                raise FeedObjectDoesNotExistException('Invalid feed id!')
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status

    @staticmethod
    def downvote_feed(feed_id: int):
        session = Session(expire_on_commit=True)
        session.connection(execution_options={'isolation_level': 'SERIALIZABLE'})
        status = False
        try:
            feed_obj = session.query(FeedModel).filter(FeedModel.id == feed_id).first()

            if feed_obj is not None:
                feed_obj.downvote += 1
                session.commit()
                status = True
            else:
                raise FeedObjectDoesNotExistException('Invalid feed id!')
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status

    @staticmethod
    def get_newsfeed(user_id: int):
        session = Session()
        news_feed_objs = []
        try:
            user_obj = session.query(UserModel).filter(UserModel.id == user_id).first()
            if user_obj is None:
                raise UserDoesNotExistException('Invalid user id!')

            feed_objs_1 = session.query(
                FeedModel.id,
                FeedModel.content,
                FeedModel.created_at,
                (FeedModel.upvote - FeedModel.downvote).label('score'),
                func.count(CommentModel.id).label('comment_sum')
            ).join(CommentModel, FeedModel.id == CommentModel.feed, isouter=True)\
                .join(FollowerModel, FeedModel.user == FollowerModel.follower, isouter=True)\
                .join(UserModel, UserModel.id == FollowerModel.user, isouter=True)\
                .filter(UserModel.id == user_id)\
                .group_by(FeedModel.id, FeedModel.content)\
                .order_by(text('score DESC'), text('comment_sum DESC'), FeedModel.created_at.desc())

            feed_obj_ids = [feed.id for feed in feed_objs_1]

            feed_objs_2 = session.query(
                FeedModel.id,
                FeedModel.content,
                FeedModel.created_at,
                (FeedModel.upvote - FeedModel.downvote).label('score'),
                func.count(CommentModel.id).label('comment_sum')
            ).join(CommentModel, FeedModel.id == CommentModel.feed, isouter=True)\
                .filter(FeedModel.id.not_in(feed_obj_ids))\
                .group_by(FeedModel.id, FeedModel.content)\
                .order_by(text('score DESC'), text('comment_sum DESC'), FeedModel.created_at.desc()).all()
            news_feed_objs.extend(feed_objs_1)
            news_feed_objs.extend(feed_objs_2)
        except Exception as e:
            print(e)
        finally:
            session.close()
        return news_feed_objs
