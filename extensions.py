from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# database 
db = SQLAlchemy()

# Json web Token 
jwt_manager = JWTManager()