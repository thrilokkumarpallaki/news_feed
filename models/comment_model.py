from . import *
from app.expcetions import CommentObjectDoesNotExistException


class CommentModel(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    feed = Column(Integer, ForeignKey('feed.id'), nullable=False)
    user = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(TEXT, nullable=False)
    upvote = Column(Integer, default=0)
    downvote = Column(Integer, default=0)
    comment_id = Column(Integer, ForeignKey('comments.id'), nullable=True)
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
    def upvote_comment(comment_id):
        session = Session(expire_on_commit=True)
        session.connection(execution_options={'isolation_level': 'SERIALIZABLE'})
        status = False
        try:
            comment_obj = session.query(CommentModel).filter(CommentModel.id == comment_id).first()

            if comment_obj is None:
                raise CommentObjectDoesNotExistException('Invalid comment id!')
            comment_obj.upvote += 1
            session.commit()
            status = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status

    @staticmethod
    def downvote_comment(comment_id):
        session = Session(expire_on_commit=True)
        session.connection(execution_options={'isolation_level': 'SERIALIZABLE'})
        status = False
        try:
            comment_obj = session.query(CommentModel).filter(CommentModel.id == comment_id).first()

            if comment_obj is None:
                raise CommentObjectDoesNotExistException('Invalid comment id!')
            comment_obj.downvote += 1
            session.commit()
            status = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status

