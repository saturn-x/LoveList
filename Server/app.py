from flask import Flask, request
from flask_cors import CORS

import sql
import json
app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/sql_dailylist')
def sql_dailylist():
    res=sql.sql_table(table="daily_dolist")
    return json.dumps(res)

@app.route('/sql_specialist',methods=['POST'])
def sql_specialist():
    args = request.get_json()["name"]
    res=sql.sql_table(table=args+"_special_dolist")
    return json.dumps(res)

@app.route('/sql_name',methods=['POST'])
def sql_name():
    args = request.get_json()["name"]
    res=sql.sql_name(args)
    return json.dumps(res)

@app.route('/add_record',methods=['POST'])
def add_recored():
    args = request.get_json()["params"]
    print("add_recored")
    print(args)
    sql.sql_add(args)
    return "成功"

@app.route('/delete_record',methods=['POST'])
def delete_record():
    args = request.get_json()["params"]
    sql.sql_delete(args)
    return "成功"

if __name__ == '__main__':
    app.run()