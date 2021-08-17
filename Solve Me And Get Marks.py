def solve(arr, n, k):
    x = 0
    y = 0
    if arr[1] - k <= arr[0]:
        x += 1
    else:
        y += 1
    for i in range(1, n - 1):
        if (arr[i - 1] + k >= arr[i] or arr[i] >= arr[i + 1] - k):
            x += 1
        else:
            y += 1
    if arr[n - 1] <= (arr[n - 2] + k):
        x += 1
    else:
        y += 1
    print(x, " students need to worry! ", end="\n")
    print(y, " students should relax!", end="\n")


n, k = map(int, input().split())
arr = []
arr = [int(item) for item in input().split()]
arr.sort()
solve(arr, n, k)
