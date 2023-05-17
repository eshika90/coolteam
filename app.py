from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://eshika:Mongodb123@cluster0.xrq9g7i.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index2.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({},{'_id':False}))
    count = len(bucket_list) + 1
    doc = {
        'num': count,
        'bucket': bucket_receive
    }
    db.bucket.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_bucket = list(db.bucket.find({},{'_id':False}))
    return jsonify({'result':all_bucket})

@app.route('/bucket/delete', methods=['POST'])
def complete_bucket():
    delete_receive = request.form['delete_give']

    db.bucket.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '수고하셨습니다!'})

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.fan.find({},{'_id':False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }
    db.fan.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.fan.find({},{'_id':False}))
    return jsonify({'result':all_comments})

@app.route('/guestbook/delete', methods=['POST'])
def delete_star():
    delete_receive = request.form['delete_give']

    db.fan.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

