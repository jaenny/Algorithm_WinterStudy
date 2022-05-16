function solution(scores) {
  var answer = new Array(scores.length);

  var rank = []; // 총점, 어려운 문제순으로, ID

  let q1 = 0;
  let q2 = 0;

  for (let i = 0; i < scores.length; i++) {
    q1 += scores[i][0];
    q2 += scores[i][1];
  }

  let difficultQuestion = q1 > q2 ? -1 : q1 < q2 ? 1 : 0;
  // 1 :q1이 더 어려움
  // -1 : q2가 더 어려움
  // 0 : 난이도 동일

  for (let i = 0; i < scores.length; i++) {
    rank.push([scores[i][0] + scores[i][1], scores[i][0], scores[i][1], i]);
  }

  let sorted_list = rank.sort(function (a, b) {
    if (a[0] > b[0]) return -1;
    else if (a[0] < b[0]) return 1;
    else {
      if (difficultQuestion == -1) {
        if (a[2] > b[2]) return -1;
        else if (a[2] < b[2]) return 1;
        else {
          if (a[3] > b[3]) return 1;
          else return -1;
        }
      } else if (difficultQuestion == 1) {
        if (a[1] > b[1]) return -1;
        else if (a[1] < b[1]) return 1;
        else {
          if (a[3] > b[3]) return 1;
          else return -1;
        }
      } else {
        if (a[3] > b[3]) return 1;
        else return -1;
      }
    }
  });

  for (let i = 0; i < sorted_list.length; i++) {
    answer[sorted_list[i][3]] = i + 1;
  }

  return answer;
}

console.log(
  solution([
    [85, 90],
    [65, 67],
    [88, 87],
    [88, 87],
    [73, 81],
    [65, 89],
    [99, 100],
    [80, 94],
  ])
);

console.log(
  solution([
    [85, 90],
    [91, 87],
    [88, 87],
  ])
);
