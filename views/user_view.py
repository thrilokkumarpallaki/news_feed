from app.models import UserModel, FollowerModel
from app.expcetions import (AuthenticationException, UserAlreadyExistException, UserRegistrationException,
                            UserDoesNotExistException, FollowerObjectCreationException)
from app.helpers import encrypt_password, validate_password


class UserView:
    @staticmethod
    def register_user(name, email, password) -> str:
        """
        Register a new user with name, email, and password.
        :param name: Name of the user, can include both first & last name.
        :param email: Email Id of the user must be unique.
        :param password: password to the user account.
        :return: SUCCESS or FAILURE
        """

        # Check if user is already exist
        user_obj = UserModel.get_user(email=email)

        if user_obj is not None:
            raise UserAlreadyExistException(f'User already exist with the email {email}')

        # Generate password hash
        password_hash = encrypt_password(password)

        user_obj = UserModel(name=name, email=email, password=password_hash)

        status = user_obj.save()

        if not status:
            raise UserRegistrationException("Oops! Something wasn't right. Please try again!")

        return 'SUCCESS'

    @staticmethod
    def login(email, password) -> dict:
        """
        Login a user with email and password.
        :param email: User email id
        :param password: User password.
        :return: SUCCESS OR FAILURE
        """

        user_obj = UserModel.get_user(email=email)

        if user_obj is None:
            raise AuthenticationException('Invalid Credentials!')

        is_matching = validate_password(pass_hash=user_obj.password, user_password=password)
        if not is_matching:
            AuthenticationException('Invalid Credentials!')

        # store user session data
        user_data = {
            'user_id': user_obj.id,
            'name': user_obj.name,
            'email': user_obj.email
        }
        return user_data

    @staticmethod
    def follow_user(user, follower_id):
        """
        This method
        :param user: Current logged-in user id.
        :param follower_id: A user id who is being followed
        :return:
        """

        # Get user object
        user_obj = UserModel.get_user(user_id=user)

        if user_obj is None:
            raise UserDoesNotExistException('User does not exist')

        user_id = user_obj.id

        # Check if the follower id is present
        is_follower_present = UserModel.is_user_present(follower_id)

        if not is_follower_present:
            UserDoesNotExistException('Follower id does not exist!')

        # Check if user is already following
        is_following = FollowerModel.is_already_following(user_id, follower_id)

        if is_following:
            return 'SUCCESS'

        # Add follower to the db
        follower_obj = FollowerModel(user=user_id, follower=follower_id)
        follower_status = follower_obj.save()

        if not follower_status:
            raise FollowerObjectCreationException('Something went wrong while creating Follower!')
        return 'SUCCESS'
