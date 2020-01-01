from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.user.model import Users
import json, hashlib

bp_login = Blueprint('login',__name__)
api = Api(bp_login)

class CreateTokenResource(Resource):

    # login and get token
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location = 'json', required = True)
        parser.add_argument('password', location = 'json', required = True)

        args = parser.parse_args()
        
        encrypted = hashlib.md5(args['password'].encode()).hexdigest()
        qry = Users.query.filter_by(username = args['username']).filter_by(password = encrypted)
        userData = qry.first()

        if userData is not None:
            userData = marshal(userData,Users.jwt_claims_fields)
            token = create_access_token(identity = userData['username'], user_claims = userData)
            return {'token' : token}, 200
        return{'status' : 'UNAUTHORIZED' , 'message' : 'username atau password salah'}, 401

class RefressTokenResources(Resource):

    # refresh token
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        token = create_access_token(identity = current_user)
        return {'token' : token}, 200
        
api.add_resource(CreateTokenResource,'/login')
api.add_resource(RefressTokenResources,'/refresh')