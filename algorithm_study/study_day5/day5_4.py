"""
N가지 종류의 화폐가 있다.
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
예를 들어 2원, 3원 단위의 화폐가 있을때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.
"""

def effective_coin(n, money, coin_list):
    coin_list.sort(reverse=True)
    count = 0
    for i in range(n):
        if money // coin_list[i] > 0:
            count += money // coin_list[i]
            money = money % coin_list[i]                    
    if money > 0:
        return -1
    return count

n, money = map(int, input().split())
coin_list = [int(input()) for i in range(n)]

result = effective_coin(n, money, coin_list)
print(result)