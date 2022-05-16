function solution(N, K) {
  // write your code in JavaScript (Node.js 8.9.4)

  let n = String(N);
  let arr = new Array(3);

  for (let i = 0; i < 3; i++) {
    arr[i] = n[i];
  }

  for (let i = 0; i < n.length; i++) {
    let num = Number(n[i]);
    for (let k = K; k > 0; k--) {
      // console.log(k);
      num += 1;
      if (num == 9 || k == 1) {
        K = k - 1;
        break;
      }
    }

    arr[i] = num;
  }

  let res = '';
  for (let i = 0; i < 3; i++) {
    res += arr[i];
  }
  return Number(res);
}
console.log(solution(512, 10));
