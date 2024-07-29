from flask import Flask, request, jsonify
from http import HTTPStatus
from database import config_postgre_sql, create_all_db

app = Flask(__name__)

@app.get("/")
def index():
    return {"msg":"Hello world"}, HTTPStatus.OK

config_postgre_sql(app)
create_all_db(app)
if __name__ == "__main__":
    app.run(debug=True)