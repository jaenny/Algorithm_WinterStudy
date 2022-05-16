function solution(array, commands) {
  var answer = [];

  commands.forEach((command) => {
    [i, j, k] = command;
    newArray = [...array];
    newArray = newArray.slice(i - 1, j);
    newArray.sort((a, b) => a - b);
    answer.push(newArray[k - 1]);
  });

  return answer;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
