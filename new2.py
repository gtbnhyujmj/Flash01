 第一行：from flask_sqlalchemy import SQLAlchemy
📦 這是什麼？
flask_sqlalchemy 是一個 Flask 的擴充套件，用來與資料庫（如 SQLite、MySQL、PostgreSQL）互動。

🔧 SQLAlchemy 是什麼？
SQLAlchemy 是 Python 最強大的 ORM（Object-Relational Mapping）框架，它可以讓你用 Python 類別操作資料表，而不是寫 SQL 語句。

第二行：from werkzeug.security import generate_password_hash, check_password_hash
📦 werkzeug 是什麼？
Werkzeug 是一個提供 WSGI 支援的 Python 庫，也是 Flask 背後的核心元件之一。

✅ 總結
套件 / 函式	用途
flask_sqlalchemy.SQLAlchemy	Flask 操作資料庫用的 ORM 工具
generate_password_hash	將密碼安全地加密（儲存在資料庫）
check_password_hash	驗證輸入的密碼是否與加密密碼相符
這兩行是建立 帳號系統（註冊/登入） 的常見基礎，結合資料庫與密碼保護。


WSGI 是啥?


ChatGPT 說：
WSGI 是 Web Server Gateway Interface 的縮寫，是 Python Web 應用程式和 Web 伺服器之間的 標準介面協定。

🧠 白話解釋
你可以這樣想：

Flask、Django 等框架 是你寫的程式，
Nginx、Gunicorn、uWSGI 等 Web 伺服器 是負責接收外部 HTTP 請求的工具，
WSGI 就是讓兩者可以合作溝通的橋樑！

 WSGI 解決了什麼問題？
在 WSGI 出現之前，不同 Web 框架（例如 Flask、Django）都用自己的方式處理請求，不相容。WSGI 統一了介面，讓：

Web 框架 不需要關心伺服器細節

伺服器 不需要知道應用邏輯

開發者可以自由選擇任意伺服器搭配任意框架，只要都支援 WSGI

🔁 互動流程（簡化圖）
swift
複製
編輯
使用者 → Nginx/Gunicorn（伺服器） → WSGI 介面 → Flask/Django（你的應用程式）→ 回傳結果
