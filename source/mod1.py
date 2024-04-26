def add(a, b):
    return a+b

def safe_add(a,b):
    if type(a) != type(b):
        print(f'{type(a)}와 {type(b)}의 자료형이 다릅니다! 다른 데이터타입의 연산은 할 수 없습니다!')
    else:
        result = add(a,b)
        return result
