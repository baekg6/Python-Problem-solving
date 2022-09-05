from collections import deque

def solution(arr):
    nums = deque(arr)
    answer = []
    
    prev = -1
    tmp = nums.popleft()
    answer.append(tmp)
    
    while nums:
        prev = tmp
        tmp = nums.popleft()
        if prev!= tmp:
            answer.append(tmp)
            
    return answer