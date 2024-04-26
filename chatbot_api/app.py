# chatbot REST API 서버 구현하기
from flask import Flask, request, jsonify, abort, render_template
import socket
import json

# 챗봇엔진서버접속정보, ip, port
host = "127.0.0.1"  # chatbot server
port = 5050

# Flask객체
app = Flask(__name__)

# ./chabot_api/templates/index.html
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# 1) chatbot server와 통신
def get_answer_from_engine(bottype, query):
    # chatbot서버와 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # chatbot서버에 request(query)
    json_data = {
        "Query": query,
        "BotType": bottype
    }

    # chatbot서버에 query전송
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # chatbot서버에서 response
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    # chatbot서버에 연결된 socket자원을 해제
    mySocket.close()

    return ret_data

# 2) chatbot엔진에 query를 전송하는 API
# http://localhost:5000/query/TEST
@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
   
    body = request.get_json()

    try:
        if bot_type == "TEST":
            # chatbot api test
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)
        elif bot_type == "KAKAO": # 카카오톡 skill
            pass
        elif bot_type == "NAVER": # 네이버톡톡 Web Hook 처리
            pass
        else:
            # 정의되지 않은 bot_type일 경우 404발생
            abort(404)
    except Exception as e:
        # 예외발생시 500에러 발생
        abort(500)
            
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # WebServer
