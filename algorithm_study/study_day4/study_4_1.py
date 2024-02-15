"""
부품 찾기
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.
N = 5
[8, 3, 7, 9, 2]
손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
M = 3
[5, 7, 9]
이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.
"""
#1 이진 탐색 안쓰고 풀어보기
N = int(input())
whole_object = list(map(int, input().split()))

M = int(input())
neccesary_object = list(map(int, input().split()))

count = 0
for object in range(M):
    if neccesary_object[object] in whole_object:
        print("yes", end=' ')
    else:
        print("no", end=' ')
print()

#2 이진 탐색 써보기