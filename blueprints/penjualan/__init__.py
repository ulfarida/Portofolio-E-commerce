from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import json, datetime, hashlib
from . import *
from blueprints import db, app
from blueprints.keranjang.model import Keranjang, KeranjangDetails
from blueprints.admin.model import Produk
from flask_jwt_extended  import jwt_required, verify_jwt_in_request, get_jwt_claims

bp_penjualan = Blueprint('penjualan',__name__)
api = Api(bp_penjualan)

class PenjualanResources(Resource):

    # lihat seluruh produk di keranjang
    @jwt_required
    def get(self):   
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        args = parser.parse_args()

        offset = (args['p']*args['rp']) - args['rp']

        claims = get_jwt_claims()

        qry_keranjang = Keranjang.query.filter_by(user_id = claims['id'])
        keranjangData = qry_keranjang.first()

        qry_keranjang_details = KeranjangDetails.query.filter_by(keranjang_id = keranjangData.id).filter_by(deleted=False)

        if qry_keranjang_details is not None:
            produks = []
            for produk in qry_keranjang_details:
                marshal_produk = marshal(produk, KeranjangDetails.response_fields)
                # marshal_produk['produk'] = marshal(Produk.query.get(marshal_produk['produk_id']), Produk.response_fields)
                produks.append(marshal_produk)

        keranjangInfo = marshal(keranjangData, Keranjang.response_fields)
        keranjangInfo['produk'] = produks
        return keranjangInfo, 200

    def options(self):
        return {}, 200

class KeranjangbyIdResources(Resource):

    # hapus produk dari keranjang
    @jwt_required
    def delete(self, id):        
        claims = get_jwt_claims()

        qry_keranjang = Keranjang.query.filter_by(user_id = claims['id'])
        keranjangData = qry_keranjang.first()

        qry_keranjang_details = KeranjangDetails.query.filter_by(keranjang_id = keranjangData.id).filter_by(deleted=False).filter_by(id = id)
        produkItem = qry_keranjang_details.first()

        if produkItem is not None:
            produkItem.deleted = True
            keranjangData.total_harga -= produkItem.harga
            db.session.commit()
            return {'message' : 'produk telah terhapus dari keranjang'}, 200
        else:
            return {'message' : 'produk tidak ditemukan'}, 404

    # lihat produk by id
    @jwt_required
    def get(self, id):        
        claims = get_jwt_claims()

        qry_keranjang = Keranjang.query.filter_by(user_id = claims['id'])
        keranjangData = qry_keranjang.first()

        qry_keranjang_details = KeranjangDetails.query.filter_by(keranjang_id = keranjangData.id).filter_by(deleted=False).filter_by(id = id)
        produkItem = qry_keranjang_details.first()

        if produkItem is not None:
            produk = marshal(produkItem, KeranjangDetails.response_fields)
            # detail_produk = marshal(Produk.query.get(produk['produk_id']), Produk.response_fields)
            # produk['produk'] = detail_produk
            return produk, 200
        else:
            return {'message' : 'produk tidak ditemukan'}, 404

    def options(self):
        return {}, 200

api.add_resource(PenjualanResources,'')
# api.add_resource(KeranjangbyIdResources, '/<int:id>')