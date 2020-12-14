from flask import Flask, g


def create_app():
    allegrosz = Flask(__name__)

    from .views import bp_main

    allegrosz.register_blueprint(bp_main)

    @allegrosz.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return allegrosz
