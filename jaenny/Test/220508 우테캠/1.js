function solution(salaries, days) {
  var answer = 0;

  salaries.forEach((salary) => {
    let day = salary[0];
    let money = salary[1];
    if (days % day == 0) {
      answer += money * parseInt(days / day);
    } else {
      answer += money * (parseInt(days / day) + 1);
    }
  });

  return answer;
}
