import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_prefixed_env()
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SECRET_KEY='dev-5a4b626e19c3e7656c7b7d93b2c8afea73ebc751fd90751cdd19ef2b73cb4a7c',
        W3_CSS_TEMPLATE = 'https://www.w3schools.com/lib/w3-theme-w3schools.css'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)

    app.add_url_rule('/', endpoint='index')

    return app
