from flask import Flask, render_template, request, redirect, url_for

# Flask = 用來建立 Flask 應用程式的主體
# request = 用來處理 HTTP 請求的物件

# render_template = 用來顯示 HTML 模板，".HTML"檔案要放templates資料夾內(注意有"s")
# redirect = 用來將使用者重新導向到另一個網址
# url_for = 根據函式名稱自動產生 URL 路徑，可以避免硬編網址。


from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy = 用來處理資料庫操作的物件


# Werkzeug 是一個提供 WSGI 支援的 Python 庫
# WSGI = Web Server Gateway Interface，是一個 Python 的標準，用來定義如何讓 Web 伺服器與 Python 應用程式溝通。
from werkzeug.security import generate_password_hash, check_password_hash
# generate_password_hash = 用來將密碼進行雜湊處理
# check_password_hash = 用來檢查密碼是否正確


# Flask實體
app = Flask(__name__)


# 設定 SQLite 資料庫路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app) # 這行建立了一個 SQLAlchemy 的實例，並綁定到這個 Flask 實例(名稱 = app) 上。

# 解釋：
# app.config 是 Flask 應用的設定字典，你可以在裡面加入各種設定。
# SQLALCHEMY_DATABASE_URI 是 SQLAlchemy 的設定鍵，用來告訴它要連接哪個資料庫。
# URI是URL的上位版本

# 'sqlite:///users.db' 是資料庫的位置與格式，這裡使用 SQLite 資料庫，並且資料庫檔案名稱為 users.db。
# 'PostgreSQL' 會不太一樣 >>> "postgresql://user:password@localhost/dbname"

# ///users.db 表示資料庫檔案在目前目錄下，叫做 users.db。
# 會產生一個db在 /instance/users.db，但是不要打instance，會掛掉。


# 使用者資料表
# 這是定義一個資料表模型 named = User。
# 它繼承自 db.Model，代表 SQLAlchemy 會把這個 Python 類別對應成一張資料表。
class User(db.Model):
    # 各欄位說明
    
    id = db.Column(db.Integer, primary_key=True) 
    # id = 資料表的主鍵，每個資料都會有唯一的 id。
    # db.Integer: 資料型別：整數
    # primary_key=True: 設定這個欄位是主鍵
    
    username = db.Column(db.String(80), unique=True, nullable=False) 
    # username = 使用者名稱，必須是唯一的，且不能為空。
    # db.String(80): 資料型別：最多 80 字的字串
    # unique=True: 這個欄位值不能重複（用來當帳號很好）
    # nullable=False: 不能是空值（必填欄位）
    
    password_hash = db.Column(db.String(128), nullable=False)
    # password_hash = 密碼的雜湊值，不能為空。
    # db.String(128): 儲存長度最多 128 的字串
    # nullable=False: 必填欄位


# 建立資料表（只需要第一次）
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

# 建立註冊頁路由
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)

        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

  app.secret_key = 'verysecret'  # 隨便設一個 secret key

  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = 'login'  # 如果未登入會導去 login 頁
