from models.user import User
from flask_restful import Resource
from http import HTTPStatus
from flask import request


class UserRegistryResource(Resource):
    
    def post(self):

        data = request.get_json()

        db_useremail = data.get('useremail')
        db_userpassword = data.get('userpassword')

        if User.get_by_useremail(mail=db_useremail):
            return {"message": "Email already in use"}, HTTPStatus.BAD_REQUEST

        hashed_pwd = User.hash_password(db_userpassword)
        user = User(
            useremail = db_useremail,
            userpassword = hashed_pwd
        )
        
        user.save()

        return user.data, HTTPStatus.CREATED

    

class UserListResource(Resource):
    def get(self):

        data = []

        for user in User.get_all_users():
            data.append(user.data)

        return {'data': data}, HTTPStatus.OK