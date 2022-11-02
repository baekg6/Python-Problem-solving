def solution(n, stages):
    
    stages.sort()

    result = {}
    for i in range(n):
        result[i+1] = 0

    index = 0
    while index < len(stages):
        if stages[index] > n:
            break
            
        count = 1
        for j in stages[index+1:]:
            if stages[index] == j:
                count+=1
            else:
                break

        result[stages[index]] = (count)/(len(stages)-index)
        index += count

    return sorted(result, key=lambda x: -result[x])