from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
db = SQLAlchemy()
migrate = Migrate()

def create_app(environment):

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    migrate.init_app(app, db)
    cors = CORS(app, resources={
        r'/api/*': {
            'origins': ["*"]
        }
    })
    from api.to_do_resources.controller import to_do_services
    app.register_blueprint(to_do_services,url_prefix='/api')
    return app
