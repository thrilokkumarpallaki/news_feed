from flask import jsonify

from app.application import application as flask_app

from . import *


@flask_app.errorhandler(UserAlreadyExistException)
def handle_user_already_exist(err):
    """
    This function handles UserAlreadyExistException thrown in the application
    and returns json object
    :param err: Error object
    :return: json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }

    return jsonify(response), err.code


@flask_app.errorhandler(UserRegistrationException)
def handle_user_already_exist(err):
    """
    This function handles UserRegistrationException thrown in the application
    and returns json object
    :param err: Error object
    :return: json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }

    return jsonify(response), err.code


@flask_app.errorhandler(AuthenticationException)
def handle_authentication_error(err):
    """
    This function handles AuthenticationException thrown in the application.
    :param err: Error object
    :return: json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }
    return jsonify(response), err.code


@flask_app.errorhandler(UserDoesNotExistException)
def handle_user_does_not_exist(err):
    """
    This function handles UserDoesNotExistException thrown in the application.
    :param err: Error object
    :return: Json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }
    return jsonify(response), err.code


@flask_app.errorhandler(FeedObjectDoesNotExistException)
def handle_feed_object_does_not_exist(err):
    """
       This function handles FeedObjectDoesNotExistException thrown in the application.
       :param err: Error object
       :return: Json error object
       """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }
    return jsonify(response), err.code


@flask_app.errorhandler(FollowerObjectCreationException)
def handle_follower_does_not_exist(err):
    """
    This function handles FollowerObjectCreationException thrown in the application.
    :param err: Error object
    :return: Json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }


@flask_app.errorhandler(FeedObjectCreationException)
def handle_feed_does_not_exist(err):
    """
    This function handles FeedObjectCreationException thrown in the application.
    :param err: Error object
    :return: Json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }


@flask_app.errorhandler(CommentObjectCreationException)
def handle_feed_does_not_exist(err):
    """
    This function handles CommentObjectCreationException thrown in the application.
    :param err: Error object
    :return: Json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }


@flask_app.errorhandler(CommentObjectDoesNotExistException)
def handle_feed_does_not_exist(err):
    """
    This function handles CommentObjectDoesNotExistException thrown in the application.
    :param err: Error object
    :return: Json error object
    """
    response = {
        'err_msg': err.description,
        'err_code': err.code
    }
