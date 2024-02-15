"""
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서
다음과 같은 2가지 경우로 이동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.

입력 조건
    - 첫째 줄에 8 x 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.
출력 조건
    - 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""
# 종이에 8 x 8 평면 그려보자.
# 사분면에 나이트가 있다고 생각하고 ㄴ 자 블럭을 90도 기준으로 돌려보면 8번이 나온다.
# ㄴ 자의 꼭지점 부분에 해당하는 곳이 제4사분면쪽에 위치하지 않는다면 이동하지 못한다고 생각하면 편한 것 같다.
# 여기서 문제를 보면 행과 열의 위치를 숫자가 아닌 숫자와 알파벳으로 가져오게된다.
# 1은 정수라서 쉬운데 a는? 이럴때 사용하는 것중 하나인 아스키코드가 있다. (참고 : https://namu.wiki/w/%EC%95%84%EC%8A%A4%ED%82%A4%20%EC%BD%94%EB%93%9C )
# 그래서 숫자와 같이 아스키코드를 변환해서 출력해주려면 a에 해당하는 아스키 코드를 빼준다음 1을 더해주면 가능하다.


# 현재 나이트의 위치 입력
knight_posi = input()

# 현재 나이트의 행과 열 구하기
# 여기서 ord 란 ? 
row = int(knight_posi[1])
column = ord(knight_posi[0]) - ord('a') + 1

# 이동 가능한 8가지 경우 계산
# 튜플안의 값은 (행, 열)
# 왜 튜플 사용? 값이 변하지 않는 고정 값들이기 때문에.
move_cases = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 이동 가능한 경우의 수 계산
count = 0

for move in move_cases:
    next_row = row + move[0]
    next_column = column + move[1]

# 이동 가능한 경우인지 확인
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

# 결과 출력
print(count)