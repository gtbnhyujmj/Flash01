# 匯入 Flask 類別，用來建立網站應用程式
# 這是從 flask 套件中匯入 Flask 類別。這個類別是建立整個網站應用的基礎。
from flask import Flask

# 建立 Flask 應用程式實例，__name__ 用來告訴 Flask 要從哪裡啟動
# 這行建立一個 Flask 應用程式的實例（物件），命名為 app。
# __name__ 是目前這個 Python 模組的名稱，用來幫 Flask 找出資源路徑等設定。
app = Flask(__name__)


# 設定當使用者造訪網站根目錄 "/" 時，要執行的函式
# 告訴 Flask：當有人瀏覽這個網站的 首頁 / 時，要執行下面的 index() 函式。
@app.route('/')
def index():
    # 回傳的字串會顯示在使用者瀏覽器上
    # 這個函式會在有人打開 / 網址時執行，並回傳文字：Hello from Flask!
    return 'Hello from Flask!'


# 如果這個檔案是直接執行（不是被其他程式引用），就啟動 Flask 伺服器
# if __name__ == '__main__':
# 這表示「只有當你直接執行這個 Python 檔案時，才會啟動 Flask 伺服器」。
if __name__ == '__main__':

    # 啟動伺服器，host='0.0.0.0' 表示允許外部連線（如 Replit 外部訪問）
    # port=5000 指定使用 5000 埠號
    app.run(host='0.0.0.0', port=5000)

# 🧠總結流程圖
# Flask 應用啟動。
# 有人連到 / 網址。
# Flask 呼叫 index() 函式。
# 回傳「Hello from Flask!」文字給使用者的瀏覽器。
