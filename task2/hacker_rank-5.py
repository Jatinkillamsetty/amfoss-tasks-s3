t = int(input())
for _ in range(t):
    s = input().strip()
    freq = [0]*10
    for ch in s:
        freq[int(ch)] += 1
    
    res = []
    for i in range(10):
        need = 9 - i
        for d in range(need, 10):
            if freq[d] > 0:
                res.append(str(d))
                freq[d] -= 1
                break
    print("".join(res))