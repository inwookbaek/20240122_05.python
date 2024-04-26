import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# openAI API 키 설정
openai.api_key = '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'

@app.route('/', methods=['GET'])
def index():
    return "Hello chatGPT"
    
@app.route('/chatbot', methods=['POST'])
def chatbot():
   
    # 1. 클라이언트로부터 메시지(발화자 질의) 받기
    user_message = request.json['message']
    print(user_message)
    
    # # 2. chatGPT에 대화 시작요청 보내기
    # response = openai.Completion.create(
    #     engine= 'text-davinci-003',  # chatGPT 3.5
    #     prompt=f'User: {user_message}\nChatGPT'
    # )
    
    # # 3. chatGPT의 응답전송
    # chatgpt_response = response['choices'][0]['text'].strip()
    
    # return jsonify({'message': chatgpt_response})
    
if __name__ == '__main__':
    app.run()
