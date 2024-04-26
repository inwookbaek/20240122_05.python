# 챗봇서버모듈
import socket

class BotServer:
    # 1. chatbot의 서버포트번화 동시접속자수를 정의
    def __init__(self, srv_port, listen_num):
        self.port = srv_port # 서버접속포트번호
        self.listen = listen_num
        self.mySock = None
        
    # 2. socket생성
    #    파이썬에서 지원하는 저수준 네트워킹인터페이스 API를 사용하기 쉽게 작성된 랩퍼함수
    #    TCP/IP 소켓생성후 접속자수 만큼 클라이언트의 연결을 수락
    def create_socket(self):
        # self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock = socket.socket()
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock
        
    # 3. 클라이언트 대기후 연결을 수락하는 메서드
    #    연결요청시 클라이언트와 통신가능한 소켓객체를 리턴
    #    반환값(conn, address)을 tuple형태로 리턴
    def ready_for_client(self):
        return self.mySock.accept()
        
    # 4. socket반환
    def get_socket(self):
        return self.mySock
