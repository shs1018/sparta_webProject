from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi
import crawling

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.aztwq.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)

#--- import 과정 완료 ---
#--- 데이터 베이스 연결 관련 ---

@app.route('/')
def home():
   return render_template('one_line.html')

@app.route("/project", methods=["POST"])
def project_post():
    name_receive = request.form['']
    comment_receive = request.form['']

    doc = {

    }
    db.homework.insert_one(doc)
    return jsonify({'':''})

@app.route("/project", methods=["GET"])
def project_get():
    comment_list = list(db.homework.find({}, {'_id': False}))
    return jsonify({'':''})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


