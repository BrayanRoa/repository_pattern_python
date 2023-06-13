from flask import Blueprint, request
from ..service.user_service import UserService

user = Blueprint("user", __name__)
user_service = UserService()


@user.route("/")
def get_all():
    """
    Get a lis of users.
    ---
    tags:
        - Users
    parameters:
        - name: page
          in: query
          type: integer
          required: false
          default: 1
        - name: per_page
          in: query
          type: integer
          required: false
          default: 15
    responses:
        200:
            description: A list of users
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
                        lastname:
                            type: string
                        age:
                            type: integer
    """
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return user_service.get_all(page, per_page), 200


@user.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    result = user_service.save_user(data)
    return result
