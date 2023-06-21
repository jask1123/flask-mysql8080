from flask import Flask, render_template

# Flaskアプリケーションのインスタンス化
app = Flask(__name__)

# ルートURLへのリクエストに対するハンドラ
@app.route('/')
def hello():
    return render_template('index.html')

# アプリケーションのエントリーポイント
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
