# import sys

# sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for test_case in range(1, T+1):
    words_ = input()
    # 거울에 비친 문자를 만들기 위한 변수 생성
    mirror_words = ''
    #replace를 사용하려고 했지만, 직접 바꾸는 게 더 편할 것 같아서 조건문을 이용 
    for i in words_:
        if i == 'b':
            mirror_words += 'd'
        elif i == 'd':
            mirror_words += 'b'
        elif i == 'p':
            mirror_words += 'q'
        elif i == 'q':
            mirror_words += 'p'
    # 거울에 비친 문자를 위해 거꾸로 출력
    print(f'#{test_case} {mirror_words[::-1]}')