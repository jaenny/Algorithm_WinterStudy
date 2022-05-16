function solution(numstrs, words) {
  var answer = [];

  const translate = [['O','()'],['I'],['Z','S','7_'],['E', 'B'],['A'],['Z','S'],['b','G'],['T','Y'],['B','E3'],['g','q']]

  let word = '425'
  let res = ''

  let queue = [''];
  let i = 0;
  while (queue) { 

    if (queue.length == 0) break;

    let w = queue.shift();

    let


  }


  return anwer;
}

console.log(
  solution(['ZASSETE', 'S4Z537B', '7_ASZEYB'], ['2455373', '425', '373', '378'])
);
console.log(solution(['ZAZZ373'], ['2422373', '5455373', '2455373']));
