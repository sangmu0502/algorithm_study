"""
가로의 길이가 N, 세로의 길아가 2인 직사각형 형태의 얇은 바닥이 있다.
태일이는 이 얇은 바닥은 1 X 2의 덮개, 2 X 1의 덮개, 2 X 2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.
"""

def fill_floor(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796
    
    return dp[N]

N = int(input())
print(fill_floor(N))
