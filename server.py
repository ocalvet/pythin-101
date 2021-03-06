from flask import Flask
import json
from api_service import ApiService
app = Flask(__name__)


@app.route("/")
def hello():
    service = ApiService()
    return service.say()


@app.route("/help", methods=["GET"])
def get_help():
    return "Here is some help!"


@app.route("/help", methods=["POST"])
def post_help():
    return json.dumps({"text": "Posting some help!"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
