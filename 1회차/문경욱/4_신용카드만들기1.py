# import sys

# sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for test_case in range(1, T+1):
    # 데이터를 list로 입력 받음
    list_ = list(map(int, input().split()))
    
    # 총합을 위한 변수 설정
    sum_ = 0

    # 홀수번째는 2배 해서 더하고, 짝수번째는 그냥 더해야 함
    # list는 0부터 시작하기 때문에 list의 짝수번째가 현실세계의 홀수번째
    for num in range(0,15):
        if num%2==0:
            sum_ += list_[num]*2
        else:
            sum_ += list_[num]

    # 총합이 10으로 나눠떨어지면 0, 나머지 숫자들은 10에서 나머지만큼 빼줌
    sum_ = 0  if sum_%10 == 0 else 10-sum_%10

    print(f'#{test_case} {sum_}')

    