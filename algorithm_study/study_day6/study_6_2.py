"""
어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 보낼 수 없다.
어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 c에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

"""
import heapq

# 도시 N, 통로 M, 시작 C
N, M, C = map(int, input().split())

# 도시와 통로 정보
graph = [[] for _ in range(N+1)]
# C에서 index 까지의 최단 거리
distance = [1e9] * (N+1)

for _ in range(M):
    # X -> Y : Z
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


# C에서 모든 도시까지의 최소 거리 -> 다익스트라
def dijkstra(start):
    # 우선순위 큐
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 우선순위 큐에서 하나 씩 뽑아서 확인
        dist, now = heapq.heappop(q)

        # 처리된 적 있다 == 최단 거리가 초기값(무한)이 아니다.
        # 처리된 적 있고, 현재 고려하는 거리보다 짧으면 갱신하지 않음
        if distance[now] < dist:
            continue

        # now와 연결된 통로 확인
        for i in graph[now]:
            # start -> now -> i[0]
            cost = dist + i[1]
            # now를 거쳐서 i[0]으로 가는 경우가 더 짧으면,
            # 그 거리로 갱신하고, 우선순위 큐에 삽입
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)

cnt, time = 0, 0
for i in range(1, N+1):
    # 무한이 아니면, 해당 도시에 전보 가능 / 자기 자신은 0이므로 제외
    # 무한이 아닌 값들 중에서 최댓값이 전체 걸리는 시간
    if distance[i] < 1e9 and distance[i] != 0:
        cnt += 1
        time = max(time, distance[i])

print(cnt, time)
