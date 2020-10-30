from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

from flask_sqlalchemy import SignallingSession
from history_meta import versioned_session, Versioned
versioned_session(SignallingSession)

app = Flask(__name__)
CORS(app)
api = Api(app)
#mail= Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:prutech@localhost/demodbnew'
print('postgres configured')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
#db.create_all()

@app.before_first_request
def create_tables():
    print('entered create tables')
    db.create_all()  # This method will create all necessary tables for us
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

import views, models, resources

api.add_resource(resources.AddEmployee,'/addemp')
api.add_resource(resources.EmployeeEdit,'/editemp')
api.add_resource(resources.AddAddress,'/addaddress')
api.add_resource(resources.AddressEdit,'/editaddress')
api.add_resource(resources.AddProduct,'/addproduct')
api.add_resource(resources.ProductEdit,'/editproduct')


if __name__=='__main__':
    app.run()