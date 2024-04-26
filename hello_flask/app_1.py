# 2. 동적으로 변수를 처리하는 방법
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask?'

# https://localhost:5000/info/홍길동
@app.route('/info/<name>')
def get_name(name):
    return f'Hello {name}'

# https://localhost:5000/JSON/1000/자장면 1개 주문할게요?
@app.route('/JSON/<int:id>/<message>')
def send_message(id, message):
    json = {
        "id": id,
        "message": message,
        "xxx": "====================>"
    }
    return json

# https://localhost:5000/손흥민/32
@app.route('/<name>/<int:age>')
def hello_user(name, age):
    return render_template('hello.html', name=name, age=age)

if __name__ == '__main__':
    app.run()
