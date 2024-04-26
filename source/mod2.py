"""
    2번째 모듈입니다!
"""
def add(a, b):
    return a + b

def safe_add(a,b):
    if type(a) != type(b):
        print(f'{type(a)}와 {type(b)}의 자료형이 다릅니다! 다른 데이터타입의 연산은 할 수 없습니다!')
    else:
        result = add(a,b)
        return result

def sub(a, b):
    return a - b

def main():
    print(f'__name__ = {__name__}')
    print(add(10,10))
    print(safe_add(10, '100'))
    print(sub(20, 10))

if __name__ == '__main__':
    main()
