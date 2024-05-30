from app.container import unitow_imp
from flask import jsonify, abort
from marshmallow import ValidationError
from ..schema.user_schema import list_users, user
from ..model.user_model import UserDTO


class UserService:
    def get_all(self, page, per_page):
        users = unitow_imp.user.list(page, per_page)
        data = list_users.dump(users[0])
        return {"data": data, "meta":users[1]}

    def save_user(self, data):
        user_data = None
        try:
            user_data = user.load(data)
            user_info = UserDTO(
                name=user_data.get("name"), 
                lastname=user_data.get("lastname"), 
                age=user_data.get("age")
            )
            user_added = user.dump(unitow_imp.user.add(user_info))
            return {
                "msg": "user cretad succesfully",
                "data": user_added,
                "code": 201,
            }, 201
        except ValidationError as e:
            abort(400, e.messages)
