N, Q = map(int,input().split())
X = list(map(int, input().split()))
bk = [0] * (N + 1)
ans = []

for x in X:
    # 0じゃない場合はそのまま入れる
    if x >= 1:
        bk[x] += 1:
        ans.append(x)
    else:
        y = min(range(1, N + 1), key=lambda j:bk[j])
        bk[y] += 1
        ans.append(y)

print(" ".join(map(str, ans)))
    