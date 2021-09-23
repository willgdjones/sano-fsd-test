# API for user authenticated endpoints
# Note: none of these endpoints should have a user_id or user_email parameter passed in via the request.
# the user_id and user_email is obtained from the JWT, if valid
import io
import json
import logging
from datetime import datetime as dt

import numpy as np
import pytz
import shortuuid
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

from core.auth.decorators import user_only
from core.models import Users, Studies, Enrollments

tz = pytz.timezone("Europe/London")
user_api = Blueprint("user_api", __name__)
logger = logging.getLogger(__name__)


# An example user authenticated endpoint.
@user_api.route("/user", methods=["GET"])
@user_only
def get_user(user_id, user_email):
    return jsonify(user_id)

@user_api.route("/user/enrollment/<study_key>", methods=["POST"])
@user_only
def enroll_user_to_study(user_id, user_email, study_key):
    user = Users.get(Users.id == user_id)
    study = Studies.get(Studies.key == study_key)
    try:
        Enrollments.create(user=user, study=study)
    except IntegrityError:
        logger.warning("The enrollment already exists.")
        return {}, 200
    else:
        return {}, 201

@user_api.route("/user/enrollment/<study_key>", methods=["DELETE"])
@user_only
def unenroll_user_from_study(user_id, user_email, study_key):
    user = Users.get(Users.id == user_id)
    study = Studies.get(Studies.key == study_key)
    try:
        Enrollments.get(user=user, study=study).delete_instance()
    except DoesNotExist:
        logger.warning("The enrollment does not exist.")
    return {}, 200
