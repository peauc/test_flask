from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)

    from models import db
    db.init_app(app)
    db.create_all(app=app)

    from views.frontend import api
    app.register_blueprint(api)

    return app
