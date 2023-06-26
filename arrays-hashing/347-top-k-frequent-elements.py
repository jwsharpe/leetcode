def solution(numbers):
    if len(numbers) == 0:
        return []
    
    count = {}
    freq = [[] for i in range(len(numbers)+1)]
    
    for n in numbers:
        count[n] = 1 + count.get(n, 0)
    
    for key in count:
        freq[count[key]].append(key)
    
    minFreq = min(freq)
    print(minFreq)
    return freq[minFreq
