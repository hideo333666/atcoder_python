N = int(input())
found = False

for i in range(1,9+1):
  if found: break
  for k in range(1, 9+1):
    if i * k == N:
      found = True
      break
    
print("Yes" if found else "No")
      