from . import *


class FollowerModel(Base):
    __tablename__ = 'followers'
    __table_args__ = (
        PrimaryKeyConstraint('user', 'follower'),
    )

    user = Column(Integer, ForeignKey('users.id'), nullable=False)
    follower = Column(Integer, ForeignKey('users.id'), nullable=False)

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
    def is_already_following(user_id, follower_id) -> bool:
        session = Session()
        is_following = False

        try:
            follower_count = session.query(FollowerModel).filter(FollowerModel.user == user_id)\
                .filter(FollowerModel.follower == follower_id).count()

            if follower_count == 1:
                is_following = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return is_following
