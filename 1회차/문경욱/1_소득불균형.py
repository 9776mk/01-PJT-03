# import sys

# sys.stdin = open("_소득불균형.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # 데이터들을 list로 입력
    n_list = list(map(int, input().split()))
    # 전체 데이터의 평균을 구함
    avg_n = sum(n_list)/N
    
    cnt = 0

    # list안의 데이터들이 평균보다 작을 경우 cnt를 +1
    for num in n_list:
        if num <= avg_n:
            cnt += 1
        else:
            continue

    print(f'#{test_case} {cnt}')