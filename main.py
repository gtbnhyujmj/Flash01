# 從 flask 套件引入建立網站的核心工具 Flask
from flask import Flask

# 建立一個 Flask 應用程式的實例（物件），命名為 app。
# __name__ 幫 Flask 知道從哪裡啟動
app = Flask(__name__)


# 當使用者造訪 "/"，執行這個函式回傳內容
@app.route('/')
def index():
    # 這個函式會在有人打開 / 網址時執行，並回傳文字：Hello from Flask!
    return 'Hello from Flask!'


# if __name__ == '__main__': # 只有直接執行這支程式時，才啟動伺服器
# 這表示「只有當你直接執行這個 Python 檔案時，才會啟動 Flask 伺服器」。
if __name__ == '__main__':

    # 直接執行時啟動伺服器，允許外部用 5000 埠連線
    # port=5000 指定使用 5000 埠號
    app.run(host='0.0.0.0', port=5000)

# 🧠總結流程圖
# Flask 應用啟動。
# 有人連到 / 網址。
# Flask 呼叫 index() 函式。
# 回傳「Hello from Flask!」文字給使用者的瀏覽器。
