# Preprocess.py(2) - 시퀀스생성로직 작성
# 단어인덱스 시퀀스변환 메서드를 추가
from konlpy.tag import Komoran
import pickle
import jpype  # JPype는 Python 으로 하여금 거의 모든 Java 라이브러리를 사용하게 한다.

class Preprocess:
    # 1. 생성자
    def __init__(self, word2index_dic='', userdic=None):
        # 0) 단어인덱스사전 로딩
        if(word2index_dic != ''):
            f = open(word2index_dic, 'rb')
            self.word_index = pickle.load(f)
            f.close()
        else:
            self.word_index = None
            
         # 1) 형태소분석기객체생성 및 초기화
        self.kormorn = Komoran(userdic=userdic)
        
        # 2) 불용어제거
        # 제외할 품사를 exclusion_tags 리스트에 정의
        # 참조 : https://docs.komoran.kr/firststep/postypes.html
        # 관계언, 기호, 어미, 접미사를 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC', 'SF', 'SP', 'SS', 'SE', 'SO', 'EP', 
            'EF', 'EC', 'ETN', 'ETM', 'XSN', 'XSV', 'XSA']  
        
    # 2. 형태소분속기 pos 태거
    def pos(self, sentence):
        jpype.attachThreadToJVM() 
        return self.kormorn.pos(sentence)
        
    # 3. 불용어제거후 필요한 품사정보만 가져오기
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list     

    # 4. 키워드를 단어인덱스 시퀀스로 변환
    def get_wordidx_sequence(self, keywords):
        if self.word_index is None:
            return []
            
        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except KeyError:
                w2i.append(self.word_index['OOV']) # 해당 단어가 사전에 없을 떄 OOV처리
                
        return w2i       
