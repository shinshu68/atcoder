n,k = map(int, input().split())
a = list(map(int, input().split()))

ans = 1;
for i in range(n):
    ans = ans * a[i]
    if ans >= 10**k:
        ans = 1

print(ans)