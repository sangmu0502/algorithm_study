"""
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대싱네 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
젉단기에 높이를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm 가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm 이다. 손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 떄 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
"""

# 이진 탐색을 사용하여 문제 해결
def binary_search(start, end, target, array):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                total += x - mid
        # 떡의 총 길이가 요청한 길이보다 작으면 높이를 낮춰야 함
        if total < target:
            end = mid - 1
        # 떡의 총 길이가 요청한 길이보다 크거나 같으면 높이를 높여도 됨
        else:
            result = mid  # 최댓값을 찾아야 하므로 일단 결과 기록 후 높이를 높임
            start = mid + 1

    return result

def result(N, M, heights):
    return binary_search(0, max(heights), M, heights)

N, M = map(int, input().split())
heights = list(map(int, input().split()))

print(result(N, M, heights))
<<<<<<< HEAD
=======

>>>>>>> 4465a3ddbdc3d86a51f702c342c8389df7424d5f
