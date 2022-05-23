from flask import Flask
from flask_restful import Api
from config import Config
from extensions import db, jwt_manager
from flask_migrate import Migrate
from resources.job import JobListResource, JobPublishResource, JobResource
from resources.token import TokenResource, TokenRefreshResource
from resources.user import UserListResource, UserRegistryResource
from models.user import User

app = Flask(__name__)
# Configuration for the APP
app.config.from_object(Config)

# Database inizialieren und DataModel migrieren
db.init_app(app)
migrate = Migrate(app, db)

# JSON Web Token 
jwt_manager.init_app(app)

# Restful api
api = Api(app)

# Endpoints for the resource
api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:jobId>")
api.add_resource(JobPublishResource, "/jobs/<int:jobId>/publish")
api.add_resource(UserRegistryResource, "/users")
api.add_resource(UserListResource, "/all_users")
api.add_resource(TokenResource, "/token")
api.add_resource(TokenRefreshResource, "/refresh")


if __name__ ==  "__main__":
    app.run(port=5000, debug=True)