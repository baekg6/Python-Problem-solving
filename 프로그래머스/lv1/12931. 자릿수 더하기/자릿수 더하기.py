def solution(n):
    answer = 0
    split_data = list(str(n))
    
    for data in split_data:
        answer += int(data)

    return answer