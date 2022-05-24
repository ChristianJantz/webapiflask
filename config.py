import db_settings

class Config:
    """
        create a separate db_settings.py file in the main directory to hide your
        the database credentials 
    """
    FLASK_DEBUG = True # Change it to Flase if it is in Production
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'+ db_settings.DB_ADMIN +':'+ db_settings.DB_PASSWORD+ '@' + db_settings.DB_HOST +'/'+ db_settings.DB_NAME +'?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = db_settings.APP_SECRET_KEY
    JWT_ERROR_MESSAGE_KEY = 'message'