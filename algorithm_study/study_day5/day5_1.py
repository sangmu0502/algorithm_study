"""
정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과 같이 4가지이다.
1. X가 5로 나누어 떨어지면, 5로 나눈다.
2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
3. X가 2로 나누어떨어지면, 2로 나눈다.
4. x에서 1을 뺀다.
정수 x가 주어졌을 때 연산 4개를 적절히 사용해서 1을 만드려고 한다.
연산을 사용하는 횟수의 최소값을 출력하시오.
"""
number = int(input())

result = 0
while number > 1:
    result += 1
    if (number % 5) == 0:
        number = number // 5
    elif (number % 3) == 0:
        number = number // 3
    elif (number % 2) > 0:
        number = number // 2
    else:
        number = number - 1 
print(result)