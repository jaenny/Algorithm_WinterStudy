function solution(answers) {
  var answer = [];

  const one = [1, 2, 3, 4, 5];
  const two = [2, 1, 2, 3, 2, 4, 2, 5];
  const thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  const score = [0, 0, 0];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === one[i % 5]) score[0] += 1;
    if (answers[i] === two[i % 8]) score[1] += 1;
    if (answers[i] === thr[i % 10]) score[2] += 1;
  }

  const maxScore = Math.max(...score);

  score.forEach((s, i) => {
    if (s === maxScore) answer.push(i + 1);
  });

  return answer;
}
