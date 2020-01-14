from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import json, datetime, hashlib
from . import *
from blueprints import db, app
from blueprints.produkseller.model import Produk
from blueprints.toko.model import Penjual
from flask_jwt_extended  import jwt_required, verify_jwt_in_request, get_jwt_claims

bp_produkseller = Blueprint('produkseller',__name__)
api = Api(bp_produkseller)

class ProdukSellerResources(Resource):

    # tambah produk
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_produk', location = 'json', required = True)
        parser.add_argument('kategori', location = 'json', required = True)
        parser.add_argument('harga', location = 'json', required = True)
        parser.add_argument('stok', location = 'json', required = True)
        parser.add_argument('deskripsi', location = 'json', required = False)
        args = parser.parse_args()

        claims = get_jwt_claims()
        qry = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry.first()
        
        produk = Produk(userData.id, args['nama_produk'], args['kategori'], args['harga'], args['stok'], args['deskripsi'], userData.lokasi)
        db.session.add(produk)
        db.session.commit()

        app.logger.debug('DEBUG : %s', produk)

        return {'message' : "produk berhasil ditambahkan!"},200

    # lihat seluruh produk
    @jwt_required
    def get(self):   
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        args = parser.parse_args()

        offset = (args['p']*args['rp']) - args['rp']

        claims = get_jwt_claims()
        qry_toko = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry_toko.first()

        if userData is not None:
            qry_produk = Produk.query.filter_by(penjual_id = userData.id).filter_by(deleted = False)

            produks = []
            for produk in qry_produk.limit(args['rp']).offset(offset).all():
                allProduk = marshal(produk, Produk.response_fields)
                produks.append(allProduk)

            return produks, 200

    def options(self):
        return {}, 200


class ProdukSellerbyIdResources(Resource):

    #edit produk
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_produk', location = 'json', required = False)
        parser.add_argument('kategori', location = 'json', required = False)
        parser.add_argument('harga', location = 'json', required = False)
        parser.add_argument('stok', location = 'json', required = False)
        parser.add_argument('deskripsi', location = 'json', required = False)
        parser.add_argument('lokasi', location = 'json', required = False)
        args = parser.parse_args()

        claims = get_jwt_claims()

        qry_toko = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry_toko.first()

        qry = Produk.query.filter_by(penjual_id = userData.id).filter_by(id = id).filter_by(deleted= False)
        produkItem = qry.first()

        if produkItem is not None:
            if args['nama_produk'] is not None:
                produkItem.nama_produk = args['nama_produk']
            if args['kategori'] is not None:
                produkItem.kategori = args['kategori']
            if args['harga'] is not None:
                produkItem.harga = args['harga']
            if args['stok'] is not None:
                produkItem.stok = args['stok']
            if args['deskripsi'] is not None:
                produkItem.deskripsi = args['deskripsi']
            if args['lokasi'] is not None:
                produkItem.lokasi = args['lokasi']

            db.session.commit()
            return {'message' : 'edit produk berhasil'}, 200

        else:
            return {'message' : 'produk tidak ditemukan'}, 404

    # hapus produk
    @jwt_required
    def delete(self, id):        
        claims = get_jwt_claims()

        qry_toko = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry_toko.first()

        qry = Produk.query.filter_by(penjual_id = userData.id).filter_by(id = id).filter_by(deleted=False)
        produkItem = qry.first()

        if produkItem is not None:
            produkItem.deleted = True
            db.session.commit()
            return {'message' : 'produk telah terhapus'}, 200
        else:
            return {'message' : 'produk tidak ditemukan'}, 404

    # lihat produk by id
    @jwt_required
    def get(self, id):        
        claims = get_jwt_claims()

        qry_toko = Penjual.query.filter_by(user_id = claims['id'])
        userData = qry_toko.first()

        qry = Produk.query.filter_by(penjual_id = userData.id).filter_by(id = id).filter_by(deleted=False)
        produkItem = qry.first()

        if produkItem is not None:
            return marshal(produkItem, Produk.response_fields), 200
        else:
            return {'message' : 'produk tidak ditemukan'}, 404

    def options(self):
        return {}, 200

api.add_resource(ProdukSellerResources,'')
api.add_resource(ProdukSellerbyIdResources, '/<int:id>')