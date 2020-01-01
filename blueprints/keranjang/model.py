# from blueprints import db
# from flask_restful import fields
# from datetime import datetime, timedelta

# class Keranjang(db.Model):
#     __tablename__ = "Keranjang"
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable = False)
#     total_harga = db.Column(db.Integer, nullable = False, default=0)

#     response_fields = {
#         'id' : fields.Integer,
#         'user_id' : fields.Integer,
#         'total_harga' : fields.Integer
#     }

#     def __init__(self, user_id, total_harga):
#         self.user_id = user_id
#         self.total_harga = total_harga

#     def __repr__(self):
#         return '<Keranjang %r>' %self.id

# class KeranjangDetails(db.Model):
#     __tablename__ = "KeranjangDetails"
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     keranjang_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable = False)
#     barang_id = db.Column(db.Integer, db.ForeignKey("Barang.id"), nullable = False)
#     kuantitas = db.Column(db.Integer, nullable = False)
#     harga = db.Column(db.Integer, nullable = False, default=0)


#     response_fields = {
#         'id' : fields.Integer,
#         'user_id' : fields.Integer,
#         'nama' : fields.String,
#         'alamat': fields.String,
#         'no_hp': fields.String,
#         'email': fields.String,
#         'tanggal_lahir': fields.DateTime,
#         'foto_profil': fields.String
#     }

#     def __init__(self, user_id, nama, alamat, no_hp, email, tanggal_lahir, foto_profil):
#         self.user_id = user_id
#         self.nama = nama
#         self.alamat = alamat
#         self.no_hp = no_hp
#         self.email = email
#         self.tanggal_lahir = tanggal_lahir
#         self.foto_profil = foto_profil

#     def __repr__(self):
#         return '<KeranjangDetails %r>' %self.id