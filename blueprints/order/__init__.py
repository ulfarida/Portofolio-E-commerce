from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import json, datetime, hashlib
from . import *
from blueprints import db, app
from blueprints.keranjang.model import Keranjang, KeranjangDetails
from blueprints.admin.model import Produk
from blueprints.transaksi.model import Transaksi
from flask_jwt_extended  import jwt_required, verify_jwt_in_request, get_jwt_claims

bp_order = Blueprint('order',__name__)
api = Api(bp_order)

class OrderResources(Resource):

    # lihat seluruh riwayat pesanan
    @jwt_required
    def get(self):   

        claims = get_jwt_claims()

        qry_transaksi = Transaksi.query.filter_by(user_id = claims['id'])
        transaksiData = qry_transaksi.first()

        qry_keranjang_details = KeranjangDetails.query.filter_by(keranjang_id = keranjangData.id).filter_by(deleted=False)

        if qry_keranjang_details is not None:
            produks = []
            for produk in qry_keranjang_details:
                marshal_produk = marshal(produk, KeranjangDetails.response_fields)
                marshal_produk['produk'] = marshal(Produk.query.get(marshal_produk['produk_id']), Produk.response_fields)
                produks.append(marshal_produk)

        keranjangInfo = marshal(keranjangData, Keranjang.response_fields)
        keranjangInfo['produk'] = produks
        return keranjangInfo, 200

    def options(self):
        return {}, 200

api.add_resource(OrderResources,'')