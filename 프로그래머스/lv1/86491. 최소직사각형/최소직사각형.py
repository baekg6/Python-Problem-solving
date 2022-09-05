def solution(sizes):
    
    large = []
    small = []
    
    for size in sizes:
        a, b = max(size), min(size)
        large.append(a)
        small.append(b)
    
    return max(large)*max(small)