from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    <h1>웹앱프로그래밍</h1>
    <p><a href="http://127.0.0.1:5000/hello">헬로 페이지</a></p>
    <p><a href="http://127.0.0.1:5000/naver">네이버 페이지</a></p>
    </body>
    </html>
    '''

@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/naver')
def naver():
    return '네이버 페이지'


if __name__ == '__main__':
    app.run()