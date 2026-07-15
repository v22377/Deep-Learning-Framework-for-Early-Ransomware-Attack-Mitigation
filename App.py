from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_model
from database import save_log

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json

    file_changes = data.get("file_changes")
    cpu = data.get("cpu")
    memory = data.get("memory")

    features = [file_changes, cpu, memory]

    result = predict_model(features)

    if result == 1:
        status = "Malicious"
    else:
        status = "Safe"

    save_log(features, status)

    return jsonify({"status": status})

if __name__ == "__main__":
    app.run(debug=True)
