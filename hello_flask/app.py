# 1. Hello Flask 출력 & Login Form 출력
# 실행 : python d:\lec\05.python\hello_flask\app.py
from flask import Flask

app = Flask(__name__)

# https://localhost:5000/
@app.route('/')
def hello():
    return 'Hello Falsk'

# https://localhost:5000/login
@app.route('/login')
def login():
    return 'Login Form'

# https://localhost:5000/chatbot
@app.route('/chatbot')
def chatbot():
    return '<h1>주문처리완료 : 주문해주셔서 감사합니다!</h1>'

if __name__ == '__main__':
    app.run()
