const zip = (a, b) => a.map((v, i) => [v, b[i]]);

function solution(n, arr1, arr2) {
    var answer = [];
    for ([i, j] of zip(arr1, arr2)) {
        let tmp = (i | j).toString(2).padStart(n, "0").replace(/1/g, "#").replace(/0/g, " ");
        console.log(tmp.length);
        // tmp = " " * (5 - tmp.length) + tmp;
        answer.push(tmp);
    }
    return answer;
}