##  문제 11724

# 정점 노드 N
# 간선 선 갯수 M
# 1<= N <=1,000
# 0<= M <=N x (N-1)/2
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N,M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: x-1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1 # 무방향 그래프

ans = 0  #연결요소갯수
chk = [False] * N


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True #  체크를 먼저해주는게 메모리 낭비 줄임
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)


print(ans)
