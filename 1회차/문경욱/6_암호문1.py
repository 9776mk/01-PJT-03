# import sys

# sys.stdin = open("_암호문1.txt")

for test_case in range(1, 11):
    N = int(input())
    origin_code = list(map(int, input().split()))
    command_num = int(input())
    command_ = list(map(str, input().split()))

    # insert 사용 a.insert(1, 'b')
    # command_ 에서 I를 만날 때마다 origin_code의 인덱스 N에(index[i+1]의 원소) index[i+3] ~ index[i+1+N2](N2는 index[i+2]의 원소) 까지 insert
    
    for i in range(len(command_)):
        # command_에서 'I'를 만나면
        if command_[i] =='I':
            # 삽입할 인덱스
            idx_ = int(command_[i+1])
            # 삽입할 숫자 갯수
            insert_num = int(command_[i+2])
            # 삽입할 문자열
            for j in range(i+3, i+3+insert_num):
                origin_code.insert(idx_, int(command_[j]))
                idx_ += 1
        else:
            continue

    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(origin_code[i], end=' ')
    print()
#  command_ I 1 5 400905 139831 966064 336948 119288 I 3 3 123456 123456 123456
#  index    0 1 2  3       4      5      6      7    8 9 10 11     12      13
#             origins_code (1)다음에  (5)개의 숫자를 삽입 (3~7)