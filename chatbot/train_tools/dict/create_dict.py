# create_dict.py(1) - 단어사전생성로직만 생성
from chatbot.utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 1. 말뭉치데이터로딩함수 -> 말뭉치데이터를 list로 변환함수
def read_corpus_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]  # 헤더를 제거
    return data
    
# 2. 말뭉치데이터로딩
corpus_data = read_corpus_data('./chatbot/train_tools/dict/corpus.txt')

# 3. 말뭉치데이터에서 키워드만 추출 -> 사용자사전리스트를 생성
# corpus_data리스트에서 POS태깅후 단어리스트(dict)에 저장
p = Preprocess()
d = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        d.append(k[0])

# 4. 사전에 사용될 index를 생성 -> 토크나이징처리를 해서 단어리스를 단어인덱스dict데이터를 생성
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(d)
word_index = tokenizer.word_index
# len(word_index)

# 5. 사전파일생성
# 생성된 단어인덱스dict(word_index)객체를 파일로 저장
f = open('./chatbot/train_tools/dict/chatbot_dict.bin', 'wb')
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()
