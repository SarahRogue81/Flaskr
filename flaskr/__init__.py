import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_prefixed_env()
    app.config.from_mapping(
        BLOG_LICENSE = 'Creative Commons Attribution-NoDerivatives 4.0 International License',
        BLOG_LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/',
        BLOG_OWNER = 'Pallets',
        BLOG_TITLE = 'Flaskr',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SECRET_KEY='dev',
        W3_CSS_TEMPLATE = 'https://www.w3schools.com/lib/w3-theme-w3schools.css',
        YEAR = 2025
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
