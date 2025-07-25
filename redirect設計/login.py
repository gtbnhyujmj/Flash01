from flask import flash, session, render_template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 從表單取得帳號密碼
        username = request.form['username']
        password = request.form['password']

        # 查詢資料庫
        user = User.query.filter_by(username=username).first()

        # 驗證密碼
        if user and check_password_hash(user.password_hash, password):
            
            # 登入成功，建立 session（或整合 flask-login）
            session['user_id'] = user.id
            
            flash('登入成功')
            return redirect(url_for('home'))
        else:
            flash('帳號或密碼錯誤')

    return render_template('login.html')
  
