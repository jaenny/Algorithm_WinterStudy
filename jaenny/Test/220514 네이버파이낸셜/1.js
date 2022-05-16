function solution(recruits, s1, s2) {
  var answer = [];

  let sCount = 0;

  let experience = [];
  let scores = [];

  for (let recruit of recruits) {
    let [ex, score] = recruit;
    experience.push(ex);
    scores.push(score);
  }
  let setExperience = new Set(experience);
  experience = [...setExperience];
  let setScores = new Set(scores);
  scores = [...setScores];

  for (let ex of experience) {
    for (let score of scores) {
      let expert = 0;
      let senior = 0;
      let junior = 0;

      for (let recruit of recruits) {
        let [curEx, curScore] = recruit;
        if (curEx >= ex && curScore >= score) expert += 1;
        else if (curEx >= s1 || curScore >= s2) senior += 1;
        else junior += 1;
      }

      if (
        expert < senior &&
        senior < junior &&
        expert > 0 &&
        senior > 0 &&
        junior > 0
      )
        answer.push([ex + score, ex, score]);
    }
  }

  answer.sort((a, b) => {
    if (a[0] > b[0]) return -1;
    else if (a[0] < b[0]) return 1;
    else {
      if (a[1] > b[1]) return -1;
      else return 1;
    }
  });

  let res = [answer[0][1], answer[0][2]];

  return res;
}
