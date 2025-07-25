@app.route('/external-login', methods=['POST'])
def external_login():
    data = request.json
    user = User.query.filter_by(external_id=data['external_id']).first()

    if not user:
        # 自動註冊
        user = User(external_id=data['external_id'], username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('dashboard'))
