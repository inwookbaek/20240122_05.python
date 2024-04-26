# 단어사전테스트
import pickle
from chatbot.utils.Preprocess import Preprocess

# 1. 단어사전로딩
f = open('./chatbot/train_tools/dict/chatbot_dict.bin', 'rb')
word_index = pickle.load(f)
f.close()

# 2. 전처리객체생성
sentence = '내일 오전 10시에 탕수육을 주문하고 싶어 ㅋㅋ'
p = Preprocess(userdic='./chatbot/utils/user_dic.tsv')
pos = p.pos(sentence)

# 3. 테스트문장을 입력값으로 전달받아서 키워드와 인덱스를 출력
keywords = p.get_keywords(pos, without_tag=True)
for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        # 해당단어가 사전에 없을 때 OOV로 처리
        print(word, word_index['OOV'])
