# import sys

# sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T+1):
    # 입력에 -가 들어가는 경우가 있으므로 split으로 나눠줌
    num_list = input().split('-')
    num_ = ''
    # 결과를 출력하기 위한 is_ok = 1로 잡음
    # True와 False로 하려고 했지만 어차피 int(False) 식으로 해야해서 그냥 int형으로
    is_ok = 1

#    print(num_list, type(num_list), len(num_list))

    # num_list의 길이가 1이 아니면, 즉 입력받은 숫자가 -로 나눠져 있었다면,
    if len(num_list) != 1:
        for i in num_list:
            # 문자열들을 한 문자열로 바꿈
            num_ += i
    else:
        # 아닌 경우 리스트 -> 문자열로 변환
        num_ += num_list[0]

 #   print(num_, len(num_))

    # 길이가 16이 아닌 경우는 0
    if len(num_) != 16:
        is_ok = 0
    # 길이가 16인 경우
    # 첫 번째 글자가 만들 수 없는 경우이면 0
    else:
        if num_[0] == '1' or num_[0] == '2' or num_[0] == '7' or num_[0] == '8' or num_[0] == '0':
            is_ok = 0
        
    print(f'#{test_case} {is_ok}')