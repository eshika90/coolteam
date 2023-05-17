from operator import length_hint
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.vby888m.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({},{'_id':False}))
    count = len(bucket_list) + 1
    doc = {
        'num': count,
        'bucket' : bucket_receive,
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '저장완료!'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.bucket.find({},{'_id':False}))
    return jsonify({'result': all_buckets})

@app.route('/bucket', methods=['POST'])
def delete_bucket():
    complete_bucket = request.form['complete_give']
    db.bucket.delete_one({'num': int(complete_bucket)})

    return jsonify({'msg': '고생하셨어요!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)