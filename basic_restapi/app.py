# 3. 기본적인 REST API 서버 구현하기
# 실행 : python d:\lec\05.python\basic_restapi\app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# 서비스리소스
resource = []

# 1) 사용자정보조회
@app.route('/user/<int:userid>', methods=['GET'])
def get_user(userid):
    for user in resource:
        if user['userid'] is userid:
            return jsonify(user)
    
# 2) 사용자추가
@app.route('/user', methods=['POST'])
def add_user():
    user = request.get_json()
    resource.append(user)
    return jsonify(resource)

if __name__ == '__main__':
    app.run()
