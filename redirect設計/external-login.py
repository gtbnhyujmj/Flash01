# 這是設計給兩個公司間彼此溝通用的。

# 直白說，A公司會把我們公司應該要知道的資料送過來，這裡假設是"POST"方法，有其他方法要注意。
# 然後，我們要把A公司丟來的資料，找我們自己的資料庫，把兩個資料核對起來。
# 然後，幫這個外來的客戶自動在我們的伺服器裡註冊一筆帳號，不然我們的伺服器裡會沒有資料。

@app.route('/external-login', methods=['POST'])
def external_login():
    data = request.json   # 假設對方的工程師很好心，把資料包好成json檔。
    user = User.query.filter_by(external_id=data['external_id']).first()   # 核對兩間公司的資料ing...

    if not user:
        # 自動註冊
        user = User(external_id=data['external_id'], username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
    
    # 假如核對成功 = 這個外部客戶其實已經是本公司的老客戶了。
    login_user(user)

    # 跳轉網頁到"使用者中心"
    return redirect(url_for('dashboard'))
