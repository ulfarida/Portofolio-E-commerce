import json, os
from datetime import timedelta
from functools import wraps

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims

app = Flask(__name__)

app.config['APP_DEBUG']=True

# ========================================
# ==================JWT===================
# ========================================

app.config['JWT_SECRET_KEY'] = 'JWjs924bG9epW02LsqwZaM309QL1tW31'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

jwt = JWTManager(app)

# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         claims = get_jwt_claims()
#         if claims['isinternal'] == False:
#             return {'status': 'FORBIDDEN', 'message' : 'Internal Only!'}, 403
#         else:
#             return fn(*args, **kwargs)
#     return wrapper

# =========================================
# ================DATABASE=================
# =========================================

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@0.0.0.0:3306/Project_Restful_API'
try :
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:alta123@0.0.0.0/Project_API_test'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:alta123@0.0.0.0/E_Commerce'
except Exception as e :
    raise e

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# ======================================
# =========IMPORT BLUEPRINT=============
# ======================================

from blueprints.register import bp_register
app.register_blueprint(bp_register,url_prefix = '/register')

from blueprints.login import bp_login
app.register_blueprint(bp_login,url_prefix = '')

from blueprints.password import bp_password
app.register_blueprint(bp_password,url_prefix = '/password')

from blueprints.profil import bp_profil
app.register_blueprint(bp_profil,url_prefix = '/profil')

db.create_all()


@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()

    log = {
        'status_code':response.status_code,
        'method':request.method,
        'code':response.status,
        'uri':request.full_path,
        'request': requestData, 
        'response': json.loads(response.data.decode('utf-8'))
    }

    if response.status_code == 200:
        app.logger.info("REQUEST_LOG\t%s", json.dumps(log))
    elif response.status_code >= 400:
        app.logger.warning("REQUEST_LOG\t%s", json.dumps(log))
    
    return response