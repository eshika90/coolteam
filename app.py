from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://eshika:Mongodb123@cluster0.xrq9g7i.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/detail_k')
def detail_k():
   return render_template('index-k.html')

@app.route('/detail_l')
def detail_l():
   return render_template('index-l.html')

@app.route('/detail_o')
def detail_o():
   return render_template('index-o.html')

@app.route("/bucket-k", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_list = list(db.bucket_k.find({},{'_id':False}))
    count = len(bucket_list) + 1
    doc = {
        'num': count,
        'bucket': bucket_receive
    }
    db.bucket_k.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/bucket-k", methods=["GET"])
def bucketk_get():
    all_bucket = list(db.bucket_k.find({},{'_id':False}))
    return jsonify({'result':all_bucket})

@app.route('/bucket-k/delete', methods=['POST'])
def completek_bucket():
    delete_receive = request.form['delete_give']

    db.bucket_k.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '수고하셨습니다!'})

@app.route("/guestbook-k", methods=["POST"])
def guestbookk_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.fan_k.find({},{'_id':False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }
    db.fan_k.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook-k", methods=["GET"])
def guestbookk_get():
    all_comments = list(db.fan_k.find({},{'_id':False}))
    return jsonify({'result':all_comments})

@app.route('/guestbook-k/delete', methods=['POST'])
def deletek_star():
    delete_receive = request.form['delete_give']

    db.fan_k.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '삭제 완료!'})

# 여기까지 김세령 세부페이지 서버

@app.route("/bucket-o", methods=["POST"])
def bucketo_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket_o.find({},{'_id':False}))
    count = len(bucket_list) + 1
    doc = {
        'num': count,
        'bucket': bucket_receive
    }
    db.bucket_o.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/bucket-o", methods=["GET"])
def bucketo_get():
    all_bucket = list(db.bucket_o.find({},{'_id':False}))
    return jsonify({'result':all_bucket})

@app.route('/bucket-o/delete', methods=['POST'])
def completeo_bucket():
    delete_receive = request.form['delete_give']

    db.bucket_o.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '수고하셨습니다!'})

@app.route("/guestbook-o", methods=["POST"])
def guestbooko_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.fan_o.find({},{'_id':False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }
    db.fan_o.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook-o", methods=["GET"])
def guestbooko_get():
    all_comments = list(db.fan_o.find({},{'_id':False}))
    return jsonify({'result':all_comments})

@app.route('/guestbook-o/delete', methods=['POST'])
def deleteo_star():
    delete_receive = request.form['delete_give']

    db.fan_o.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '삭제 완료!'})

# 여기까지 오동환님 서버

@app.route("/bucket-l", methods=["POST"])
def bucketl_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket_l.find({},{'_id':False}))
    count = len(bucket_list) + 1
    doc = {
        'num': count,
        'bucket': bucket_receive
    }
    db.bucket_l.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/bucket-l", methods=["GET"])
def bucketl_get():
    all_bucket = list(db.bucket_l.find({},{'_id':False}))
    return jsonify({'result':all_bucket})

@app.route('/bucket-l/delete', methods=['POST'])
def completel_bucket():
    delete_receive = request.form['delete_give']

    db.bucket_l.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '수고하셨습니다!'})

@app.route("/guestbook-l", methods=["POST"])
def guestbookl_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.fan_l.find({},{'_id':False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }
    db.fan_l.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook-l", methods=["GET"])
def guestbookl_get():
    all_comments = list(db.fan_l.find({},{'_id':False}))
    return jsonify({'result':all_comments})

@app.route('/guestbook-l/delete', methods=['POST'])
def deletel_star():
    delete_receive = request.form['delete_give']

    db.fan_l.delete_one({'num': int(delete_receive)})

    return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

