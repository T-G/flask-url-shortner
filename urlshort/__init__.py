from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__)
    app.secret_key = "6eed8eca96316ec9d281b4a0f80d9da3"

    from . import urlshort
    app.register_blueprint(urlshort.urlshort_bp)
    return app


    