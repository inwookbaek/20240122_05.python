from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    
    response = openai.Completion.create(
        engine= 'text-davinci-003',  # chatGPT 3.5       
        prompt=user_input,
        max_tokens=150  # 원하는 토큰의 갯수를 임의로 정의
    )
    
    bot_reply = response['choices'][0]['text'].strip()
    
    return render_template("index.html", user_input=user_input, bot_reply=bot_reply)

if __name__ == '__main__':
    app.run()
