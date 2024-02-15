"""
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

첫 번째 줄에 학생의 수 N이 입력된다. (1<= N<= 100,000)
두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
"""
# dict로 풀려고 했으나 실패
# n = int(input()) # n은 학생수 
# student_list = [0] * n

# for i in range(n):
#     student_list[i] = list(map(str, input().split()))

# compare_num = student_list[0][1]
# compare_list = student_list[0]

# for i in range(n):
#     length = n - 1
#     for num in range(1, length):
#         if int(student_list[num][1]) <= int(student_list[num - 1][1]):
#             compare_num = student_list[num -1][1]
#             compare_list = student_list[num - 1]
#             student_list[num-1] = student_list[num]
#             student_list[num][1] = compare_list
#     print(f'{student_list[i][0]}')

n = int(input())  # 학생 수

student_list = []  # 학생 정보를 저장할 리스트

# 학생 정보 입력받기
for i in range(n):
    student_info = input().split()
    # student_list.append((student_info[0], int(student_info[1])))
    student_list += [(student_info[0], int(student_info[1]))]

# 성적을 기준으로 정렬
for i in range(n):
    for j in range(1, n - i):
        if student_list[j][1] < student_list[j - 1][1]:
            # 성적이 낮은 순서로 정렬
            student_list[j], student_list[j - 1] = student_list[j - 1], student_list[j]

# 정렬된 순서대로 학생 이름 출력 
for student in student_list:
    print(f'{student[0]}', end =' ')