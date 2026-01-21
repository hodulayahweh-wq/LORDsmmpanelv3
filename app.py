from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_URL = "https://justanotherpanel.com/api/v2"
API_KEY = "d1260258cc3e3a90780911b18d922c69"


def smm_request(data):
    payload = {
        "key": API_KEY,
        **data
    }
    r = requests.post(API_URL, data=payload, timeout=30)
    return r.json()


@app.route("/")
def home():
    return "SMM Panel API Çalışıyor ✅"


@app.route("/services")
def services():
    return jsonify(smm_request({"action": "services"}))


@app.route("/balance")
def balance():
    return jsonify(smm_request({"action": "balance"}))


@app.route("/order", methods=["POST"])
def order():
    data = request.json
    data["action"] = "add"
    return jsonify(smm_request(data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
