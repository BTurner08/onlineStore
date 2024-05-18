from flask import Flask,request
import json
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"


#create another API that redirects you to a test
@app.get("/test")
def test():
    return "Hello from the test"


@app.route("/server")
def server():
    server=request.environ.get("SERVER_SOFTWARE")
    return server


@app.get("/api/about")
def about():
    myname={"name": "Blake Turner"}
    return json.dumps(myname)

products = []
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def save_product():
    newItem = request.get_json()
    print(newItem)
    # products.append(newItem)
    db.products.insert_one(newItem)
    return json.dumps(fix_id(newItem))

@app.get("/api/products")
def get_product():
    return json.dumps(products)

app.run(debug=True)