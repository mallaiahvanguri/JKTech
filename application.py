from flask import Flask, request, jsonify
from http import HTTPStatus

app = Flask(__name__)

@app.get("/")
def index():
    return {"msg":"Hello world"}, HTTPStatus.OK

if __name__ == "__main__":
    app.run(debug=True)