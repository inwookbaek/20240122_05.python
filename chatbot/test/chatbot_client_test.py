# chatbot 클라이언트 테스트 프로그램
import socket
import json

# 1. 쳇봇엔진서버접속정보
host = "127.0.0.1"
port = 5050

# 2. 클라이언트프로그램 Start
while True:
    query = input('질문을 입력하세요(작업종료는 q) => ') # 발화자의 질의
    print(f'발화자질문 : {query}')
    if(query=='q'): exit(0)

    print('='*60)
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 1) 챗봇엔진에 질의 요청
    json_data = {
        "Query": query,
        "BotType": "myBotService"
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 2) 쳇본엔진에 답변출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)
    print(f"답변 = {ret_data['Answer']}")
    print(type(ret_data), ret_data)

    # 3) 챗봇서버에 연결될 소켓 해제
    mySocket.close()
