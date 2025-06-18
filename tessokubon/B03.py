n = int(input())
a = list(map(int, input().split()))
found = False

for i in range(n):
  # 1回目2回目のループ処理を抜け出すためにbreak
  if found: break
  # indexを+1することで異なる商品を担保
  for j in range(i+1, n):
    if found: break
    # indexを+1することで異なる商品を担保
    for k in range(j+1, n):
      if a[i] + a[j] + a[k] == 1000:
        found = True
        break
      
print("Yes" if found else "No")