from blueprints import db
from flask_restful import fields
from datetime import datetime, timedelta

class Penjual(db.Model):
    __tablename__ = "Penjual"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable = False, unique=True)
    nama_toko = db.Column(db.String(255), nullable = True)
    lokasi = db.Column(db.String(255), nullable = True)

    response_fields = {
        'id' : fields.Integer,
        'user_id' : fields.Integer,
        'nama_toko' : fields.String,
        'lokasi': fields.String
    }

    def __init__(self, user_id, nama_toko, lokasi):
        self.user_id = user_id
        self.nama_toko = nama_toko
        self.lokasi = lokasi

    def __repr__(self):
        return '<Penjual %r>' %self.id