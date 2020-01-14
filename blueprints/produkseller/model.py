from blueprints import db
from flask_restful import fields
from datetime import datetime, timedelta

class Produk(db.Model):
    __tablename__ = "Produk"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    penjual_id = db.Column(db.Integer, db.ForeignKey("Penjual.id"), nullable = False)
    nama_produk = db.Column(db.String(1000), nullable = False)
    kategori = db.Column(db.String(255), nullable = False)
    harga = db.Column(db.Integer, nullable = False)
    stok = db.Column(db.Integer, nullable = False)
    deskripsi = db.Column(db.String(2000), nullable = True)
    jumlah_terjual = db.Column(db.Integer, nullable = False, default=0)
    rating = db.Column(db.Integer, nullable = False, default=0)
    lokasi = db.Column(db.String(255), nullable = False)
    deleted = db.Column(db.Boolean, nullable = False, default=False)

    response_fields = {
        'id' : fields.Integer,
        'penjual_id'  : fields.Integer,
        'nama_produk' : fields.String,
        'kategori': fields.String,
        'harga': fields.Integer,
        'stok': fields.Integer,
        'deskripsi': fields.String,
        'jumlah_terjual': fields.Integer,
        'rating': fields.Integer,
        'lokasi': fields.String
    }

    def __init__(self, penjual_id,  nama_produk, kategori, harga, stok, deskripsi, lokasi):
        self.penjual_id = penjual_id         
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.deskripsi = deskripsi
        self.lokasi = lokasi

    def __repr__(self):
        return '<Produk %r>' %self.id

class FotoProduk(db.Model):
    __tablename__ = "FotoProduk"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    produk_id = db.Column(db.Integer, db.ForeignKey("Produk.id"), nullable = False)
    foto_produk = db.Column(db.String(1000), nullable = False)
    deleted = db.Column(db.Boolean, nullable = False, default=False)

    response_fields = {
        'id' : fields.Integer,
        'produk_id'  : fields.Integer,
        'foto_produk' : fields.String
    }

    def __init__(self, produk_id,  foto_produk):
        self.produk_id = produk_id         
        self.foto_produk = foto_produk

    def __repr__(self):
        return '<FotoProduk %r>' %self.id

