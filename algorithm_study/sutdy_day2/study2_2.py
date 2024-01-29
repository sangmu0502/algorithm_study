"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
    - 00시 00분 03초
    - 00시 13분 30초
반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.
    - 00시 02분 55초
    - 01시 27분 45초

입력 조건:
    - 첫째 줄에 정수 N이 입력된다. (0 <= N <= 23)
출력 조건:
    - 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""

# 정수 N 입력
n = int(input())

# 변수 경우의 수 설정
count = 0

# n시 까지 설정. 0시, 1시, ........., n시 까지 있으므로 n + 1 로 설정
# for문의 가장 시작 부분은 가장 포괄적인 부분을 말함
for hour in range(n + 1):
# minute, second 는 60분, 60초까지 있음.
    for minute in range(60):
        for second in range(60):
            # 시, 분, 초 중에 3이 하나라도 포함되어 있는 경우 경우의 수 증가
            # TypeError: 'in <string>' requires string as left operand, not int
            # '3'을 3이라고 사용하면 문자열은 iterable하지만 정수는 iterable하지 않기 때문에 오류가 나옴. 그러므로 문자열로 '3'을, hour, minute, second를 str로 명시적 형변환을 해주어야 한다.
            if '3' in str(hour):
                    count += 1
            elif '3' in str(minute):
                    count += 1
            elif '3' in str(second):
                    count += 1

# 결과 출력
print(count)
