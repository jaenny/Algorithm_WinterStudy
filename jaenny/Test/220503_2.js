function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  if (S.length <= 2) return S;

  let arr = new Array(S.length);

  for (let i = 0; i < S.length; i++) {
    arr[i] = S[i];
  }

  for (let i = arr.length - 1; i >= 2; i--) {
    if (arr[i] === arr[i - 1] && arr[i - 1] === arr[i - 2]) {
      arr[i] = ' ';
    }
  }

  // console.log(arr);
  let res = '';
  for (let i = 0; i < S.length; i++) {
    if (arr[i] !== ' ') res += arr[i];
  }

  return res;
}
console.log(solution('eedaaad'));
