from marshmallow import fields, Schema


class UserCreation(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    age = fields.Int(required=True)


create_user_schema = UserCreation()
