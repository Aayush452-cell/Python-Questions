t = int(input())
for _ in range(t):
    strs, k = map(str, input().split(' '))
    k = int(k)
    cnt = []
    cnt.append(1)
    for i in range(1, len(strs)):
        if strs[i - 1] == strs[i]:
            cnt.append(cnt[i - 1] + 1)
        else:
            cnt.append(1)
    ans = strs[0]
    for i in range(1, len(strs)):
        if cnt[i] >= 2:
            while (cnt[i] > 1):
                ans += ans
                cnt[i] -= 1
        ans += strs[i]
    print(ans)
    if (k > len(ans)):
        print("-1")
    else:
        print(ans[k - 1])
