from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import json, datetime, hashlib
from . import *
from blueprints import db, app
from blueprints.transaksi.model import Transaksi, TransaksiDetails
from flask_jwt_extended  import jwt_required, verify_jwt_in_request, get_jwt_claims

bp_transaksi = Blueprint('transaksi',__name__)
api = Api(bp_transaksi)

class TransaksiResources(Resource):

    # tambah produk ke keranjang
    @jwt_required
    def get(self):

        claims = get_jwt_claims()
        qry_transaksi = Transaksi.query.filter_by(user_id = claims['id'])

        if qry_transaksi is not None:
            list_transaksi = []
            for transaksi in qry_transaksi:
                marshal_transaksi = marshal(transaksi, Transaksi.response_fields)
                list_transaksi.append(marshal_transaksi)

            return list_transaksi, 200

    def options(self):
        return {}, 200

api.add_resource(TransaksiResources,'')