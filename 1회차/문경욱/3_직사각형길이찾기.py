# import sys

# sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for test_case in range(1, T+1):
    # list에 input 받음
    list_N = list(map(int, input().split()))
    rest_len = 0
    # 만약 세 개의 값이 같다면 나머지 길이도 똑같음
    if list_N[0] == list_N[1] == list_N[2]:
        rest_len = list_N[0]
    
    # 3개의 값이 같지 않다면
    else: 
        len_dict = {}
        # 딕셔너리에 길이와 그 길이의 횟수를 저장
        for num in list_N:
            len_dict[num] = len_dict.get(num, 0) +1

        # 횟수가 1개가 나온 키 값을 출력해야함
        for k, i in len_dict.items():
            if i == 1:
                rest_len = k

    print(f'#{test_case} {rest_len}')