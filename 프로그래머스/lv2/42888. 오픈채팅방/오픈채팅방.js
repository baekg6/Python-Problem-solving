function solution(record){
    let answer = []
    let userInfo = {}
    for (const i of record){
        const [state, id, nickname] = i.split(' ')
        if (state === 'Enter'){
            userInfo[id] = nickname
            answer.push([id, '님이 들어왔습니다.'])
        } else if (state === 'Leave'){
            answer.push([id, '님이 나갔습니다.'])
        } else if (state === 'Change'){
            userInfo[id] = nickname
        }
    }
    //console.log(userInfo)
    answer = answer.map(item => userInfo[item[0]] + item[1])
    return answer
}