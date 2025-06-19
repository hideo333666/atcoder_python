n = int(input())
t = input()
a = input()
found = False

for i in range(n):
    if t[i] == "o" and a[i] == "o":
        found = True
    
print("Yes" if found else "No")