"""
하나의 수열에는 다양한 수가 존재한다.
이러한 수는 크기에 상관없이 나열되어 있다.
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.

첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
둘째 줄부터 N + 1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의 자연수이다.

입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.
"""

# n = int(input())   # 숫자의 개수를 n 만큼 받기.

# num_list = [0] * n   # 입력받은 n개의 숫자를 저장해줄 list 인 길이가 n인 num_list 만들기
# compare_num = num_list[0]   # 값을 비교해 줄 변수인 compare_num 초기화

# for i in range(n):   # i가 그냥 적합한 것 같아서 써 넣음
#     num_list[i] = int(input())  # num_list 에 넣어줄 n개의 숫자를 입력받아서 넣어주기

# for num in range(n):   # 숫자를 내림차순으로 만들어 줄 for문
#     length = n - num   # length 는 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 로 출력
#     for num2 in range(1, length): # 1번째 값이랑 두번째 값을 비교해서 두번째 값이 크면 첫번째 값을 compare_num에 입력해주고 첫번째 값에 두번째 값을 넣어준 다음에 두번째 값에 저장해준 compare_num 을 입력해준다. 
#         if num_list[num2 - 1] <= num_list[num2]:    # 그러면 가장 낮은 값은 오른쪽으로 이동하고 그것을 length만큼 반복.
#             compare_num = num_list[num2 - 1]    # 쉽게말해서 가장 낮은 숫자를 가장 오른쪽으로 보내고 그것을 10번 반복.
#             num_list[num2 - 1], num_list[num2] = num_list[num2], num_list[num2 - 1]
#             num_list[num2] = compare_num
    
# print(num_list)    

n = int(input())   # 숫자의 개수를 n 만큼 받기.

num_list = [0] * n   # 입력받은 n개의 숫자를 저장해줄 list 인 길이가 n인 num_list 만들기

for i in range(n):   # i가 그냥 적합한 것 같아서 써 넣음
    num_list[i] = int(input())  # num_list 에 넣어줄 n개의 숫자를 입력받아서 넣어주기

for num in range(n):   # 숫자를 내림차순으로 만들어 줄 for문
    length = n - num   # length 는 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 로 출력
    for num2 in range(1, length): # 1번째 값이랑 두번째 값을 비교해서 두번째 값이 크면 첫번째 값을 compare_num에 입력해주고 첫번째 값에 두번째 값을 넣어준 다음에 두번째 값에 저장해준 compare_num 을 입력해준다. 
        if num_list[num2 - 1] <= num_list[num2]:    # 그러면 가장 낮은 값은 오른쪽으로 이동하고 그것을 length만큼 반복.
            num_list[num2 - 1], num_list[num2] = num_list[num2], num_list[num2 - 1]

for i in range(n):            
    print(f'{num_list[i]}', end=' ')    