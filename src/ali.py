
from flask import Flask, make_response, jsonify
from flask_cors import CORS

from src.mongo import MyMongoClient

app = Flask(__name__)
CORS(app)
HOSTS = [
    "mymongo-0.mymongo.ali.svc.cluster.local:27017",
    "mymongo-1.mymongo.ali.svc.cluster.local:27017",
    "mymongo-2.mymongo.ali.svc.cluster.local:27017"
]
REPLICA_SET = "rs0"
DB_NAME = "aliyun"  # 要操作的数据库

hosts_str = ",".join(HOSTS)
uri = f"mongodb://{hosts_str}/?replicaSet={REPLICA_SET}"

mymongo = MyMongoClient(uri, DB_NAME)


@app.route('/datas', methods=['GET'])
def get_datas():
    products = mymongo.get_all('products')
    products = list(products)
    return make_response(jsonify(products=products), 200)


@app.route('/data/<id>', methods=['GET'])
def get_data(id: int):
    product = mymongo.get_one('products', {'_id': int(id)})
    return make_response(jsonify(product=product), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
