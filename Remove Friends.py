def deletek(arr, n, k):
    st = []
    st.append(arr[0])
    top = 0
    count = 0
    for i in range(1, n):
        while (len(st) != 0 and count < k and st[top] < arr[i]):
            st.pop()
            count += 1
            top -= 1
        st.append(arr[i])
        top += 1
    if count < k:
        while (count < k):
            st.pop()
            count += 1
    for i in range(0, len(st)):
        print(st[i], " ", end="")
    print()


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = []
    arr = [int(item) for item in input().split()]
    deletek(arr, n, k)
