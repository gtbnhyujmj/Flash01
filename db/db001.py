# 存放GPT設計好的資料表，未來可以複製貼上直接用。

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))
  
    email = db.Column(db.String(120), unique=True)

    # 串其他公司的ID搞兩公司資料關聯用的
    external_id = db.Column(db.String(128))  # 他公司傳來的使用者ID
    
    # 這個帳號創造的時間註記
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
