from flask import request
from flask_jwt_extended import jwt_required, get_raw_jwt, get_jwt_identity, jwt_refresh_token_required, \
    create_access_token
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from app.main.service.blacklist_service import BlackList
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        # return Auth.login_user(data=post_data)
        return Auth.login_user2(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """

    @api.doc('logout a user')
    @jwt_required
    def post(self):
        # get auth token
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        BlackList.save_token(jti)
        return {"message": "User <id={}> successfully logged out.".format(user_id)}, 200


@api.route('/refresh')
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
