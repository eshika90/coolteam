from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://eshika:Mongodb123@cluster0.7qbzrft.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detailpage')
def info():
    return render_template('index2.html')

@app.route("/detailpage_cheer", methods=["POST"])
def detailpage_cheer_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST 연결 완료!'})

@app.route("/detailpage_allcheer", methods=["GET"])
def detailpage_allcheer_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)