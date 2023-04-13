import logging
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route("/healthcheck")
    def healthcheck():
        return jsonify({"status": "ok"})

        # Configure logging for Waitress

    logger = logging.getLogger("waitress")
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)
