class APIError(Exception):
    """
    All custom API exceptions
    """


class UserAlreadyExistException(APIError):
    code = 400
    description = 'User already exists!'


class UserRegistrationException(APIError):
    code = 500
    description = 'Unable to register user!'


class AuthenticationException(APIError):
    code = 400
    description = 'User does not exist!'


class UserDoesNotExistException(APIError):
    code = 400
    description = 'Invalid Follower!'


class FeedObjectDoesNotExistException(APIError):
    code = 400
    description = 'Invalid feed object!'


class FeedObjectCreationException(APIError):
    code = 500
    description = 'Feed is not created successfully!'


class CommentObjectCreationException(APIError):
    code = 500
    description = 'Comment is not created successfully!'


class CommentObjectDoesNotExistException(APIError):
    code = 400
    description = 'Invalid comment object!'


class FollowerObjectCreationException(APIError):
    code = 500
    description = 'Follower is not created successfully!'
