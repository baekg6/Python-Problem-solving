def solution(arr):
    try: 
        answer = sum(arr)/ len(arr)
    except:
        print('1개 이상의 요소를 가진 배열을 입력하세요.')
    return answer