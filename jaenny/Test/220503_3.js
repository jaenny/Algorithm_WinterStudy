function solution(S) {
  let arr = new Array();
  arr.push([S[0]]);

  for (let i = 1; i < S.length; i++) {
    let word = S[i];
    let newArr = new Array();

    for (let j = 0; j < arr.length; j++) {
      let prev = arr[j];

      if (prev[prev.length - 1].includes(word)) {
        let temp = [...prev, word];
        newArr.push(temp);
      } else {
        let temp = [...prev, word];
        newArr.push(temp);

        prev[prev.length - 1] += word;
        newArr.push(prev);
      }
    }
    arr = newArr;
  }

  arr.sort((a, b) => a.length - b.length);
  let minLength = arr[0].length;
  let cnt = 0;

  for (let a of arr) {
    if (a.length == minLength) cnt += 1;
    else break;
  }

  return cnt;
}
console.log(solution('cycle'));
