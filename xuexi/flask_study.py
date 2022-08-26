# coding=utf-8
from flask import Flask
from flask import request
import json

app = Flask("__name__")


@app.route("/")
def Home():
    data = json.dumps({
        "username": "chengwenzhe",
        "password": "123456789"
    })
    return data


@app.route("/login", methods=["GET"])
def Login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data = json.dumps({
            "username": username,
            "password": password,
            "code": "200",
            "message": "登陆成功！",
            "info": "www.baidu.com"
        })
    else:
        data = json.dumps({
            "code": "500",
            "message": "请传递参数！"
        })
    return data


@app.route("/post_login", methods=["POST"])
def post_login():
    global data
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            data = json.dumps({
                "username": username,
                "password": password,
                "code": "200",
                "message": "登陆成功！",
                "info": "www.baidu.com"
            })
        else:
            data = json.dumps({
                "code": "500",
                "message": "参数不合法！"
            })
    return data


if __name__ == "__main__":
    app.run()
