from app.ext import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(
        required=True,
        error_messages={"required": "the name is required"}
    )
    lastname = fields.String(
        required=True, error_messages={"required": "the lastname is required"}
    )
    age = fields.Integer(required=True)


user = UserSchema()
list_users = UserSchema(many=True)
