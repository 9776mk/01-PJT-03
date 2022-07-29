# import sys

# sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(1, T+1):
    test_N = int(input())
    n_list = list(map(int, input().split()))

    n_dict = {}
    #  만약 딕셔너리에 number가 있으면 +1, 없으면 0으로 초기화한뒤 +1
    for number in n_list:
        n_dict[number] = n_dict.get(number, 0) + 1
    # 최댓값을 구하기 위해 최댓값 k,v를 설정
    max_k = -1
    max_v = 0

    for k, v in n_dict.items():
        # 현재의 갯수가 max_v 보다 크면 max_v와 max_k 를 갱신 현재 값으로
        if v > max_v:
            max_k = k
            max_v = v
        # 만약 둘이 같을 경우 더 큰 점수, k를 max_k로 넣기
        elif v == max_v:
            if k > max_k:
                max_k = k
                max_v = v
        else:
            continue

    print(f'#{test_N} {max_k}')