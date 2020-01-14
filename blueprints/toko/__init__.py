from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import json, datetime, hashlib
from . import *
from blueprints import db, app
from blueprints.toko.model import Penjual
from flask_jwt_extended  import jwt_required, verify_jwt_in_request, get_jwt_claims
from password_strength import PasswordPolicy

bp_profiltoko = Blueprint('profiltoko',__name__)
api = Api(bp_profiltoko)

class TokoResources(Resource):

    # register toko
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_toko', location = 'json', required = True)
        parser.add_argument('lokasi', location = 'json', required = True)
        args = parser.parse_args()

        claims = get_jwt_claims()
        
        penjual = Penjual(claims['id'], args['nama_toko'], args['lokasi'])
        try :
            db.session.add(penjual)
            db.session.commit()
            app.logger.debug('DEBUG : %s', penjual)
        except Exception as e:
            return {'message' : "anda sudah melakukan registrasi toko sebelumnya"},401

        return {'message' : "registrasi toko berhasil!"},200

    #edit profil toko
    @jwt_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_toko', location = 'json', required = False)
        parser.add_argument('lokasi', location = 'json', required = False)
        args = parser.parse_args()

        claims = get_jwt_claims()
        
        qry = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry.first()

        if args['nama_toko'] is not None:
            userData.nama_toko = args['nama_toko']
        if args['lokasi'] is not None:
            userData.lokasi = args['lokasi']

        db.session.commit()

        return{'message' : 'edit profil toko berhasil'}, 200

    # lihat profil toko
    @jwt_required
    def get(self):        
        claims = get_jwt_claims()

        qry = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry.first()

        profil = marshal(userData, Penjual.response_fields)

        return profil, 200

    def options(self):
        return {}, 200

api.add_resource(TokoResources,'')