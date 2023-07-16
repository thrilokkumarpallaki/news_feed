from __future__ import annotations

from . import *
from app.enums.user_status import UserStatus


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE)
    feed_items = relationship('FeedModel')
    followers = relationship('FollowerModel', foreign_keys="[FollowerModel.follower]")
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    last_modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def save(self) -> bool:
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
    def get_user(user_id: int = None, email: str = None) -> UserModel:
        session = Session()
        user_obj = None
        try:
            base_query = session.query(UserModel)

            if user_id is not None:
                user_obj = base_query.filter(UserModel.id == user_id).first()
            else:
                user_obj = base_query.filter(UserModel.email == email).first()
        except Exception as e:
            print(e)
        finally:
            session.close()
        return user_obj

    @staticmethod
    def is_user_present(user_id: int) -> bool:
        session = Session()
        is_present = False
        try:
            user_count = session.query(UserModel).filter(UserModel.id == user_id).count()
            if user_count == 1:
                is_present = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return is_present
