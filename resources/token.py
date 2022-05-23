from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from models.user import User

class TokenResource(Resource):

    def post(self):
        data = request.get_json()
        f_useremail = data.get('useremail')
        f_userpassword = data.get('userpassword')

        user = User.get_by_useremail(f_useremail)

        if not user:
            return {"message": "LOGIN useremail is incorrect"}, HTTPStatus.UNAUTHORIZED

        # if User.verify_password(f_userpassword, user.userpassword):
        #     return {"message": "LOGIN password is incorrect"}, HTTPStatus.UNAUTHORIZED
        
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(identity=user.id)

        return {"access_token": access_token, "refresh_token": refresh_token}, HTTPStatus.OK

class TokenRefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):

        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=False)

        return {"access_token" : access_token}, HTTPStatus.OK