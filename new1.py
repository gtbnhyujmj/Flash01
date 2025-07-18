🧠 簡單舉例說明用途
python
複製
編輯
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # 顯示首頁

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")  # 取得使用者輸入
    if username == "admin":
        return redirect(url_for("dashboard"))  # 登入成功就轉去 dashboard
    return "Login Failed"

@app.route("/dashboard")
def dashboard():
    return "Welcome to the dashboard!"


✅ 總結
這行引入的東西都屬於 Flask 框架中的核心工具，幫助你：

建立網頁伺服器（Flask）

顯示 HTML 頁面（render_template）

取得使用者輸入（request）

轉跳到其他頁面（redirect, url_for）

如果你正在做 Flask 專案，這是非常常見的基本組合。
