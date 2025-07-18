🧪 一個簡單的原生 WSGI 範例（不用框架）
python
複製
編輯
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello WSGI!"]
這段程式就是一個合法的 WSGI 應用程式。你可以用像 gunicorn 這樣的伺服器來執行它：

bash
複製
編輯
gunicorn myapp:application

✅ 小結
名稱	說明
WSGI	Python 的 Web 應用與 Web 伺服器之間的通訊標準
作用	讓伺服器（如 Gunicorn）與應用程式（如 Flask）可以互通
例子	Flask 是一個 WSGI 應用，可以直接被 Gunicorn 或 uWSGI 執行

如果你以後要把 Flask 應用部署到網路上，像使用 gunicorn app:app，你就是在用 WSGI 的力量。
