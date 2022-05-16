function solution(cities, roads, cars, customers) {
  var answer = [];

  const matrix = Array.from(Array(cities.length), () =>
    Array(cities.length).fill(Infinity)
  );

  for (let road of roads) {
    road = road.split(' ');
    let from = cities.indexOf(road[0]);
    let to = cities.indexOf(road[1]);
    let weight = Number(road[2]);

    matrix[from][to] = weight;
    matrix[to][from] = weight;
  }

  for (let k = 0; k < cities.length; k++) {
    matrix[k][k] = 0;
    for (let i = 0; i < cities.length; i++) {
      for (let j = 0; j < cities.length; j++) {
        if (matrix[i][j] > matrix[i][k] + matrix[k][j])
          matrix[i][j] = matrix[i][k] + matrix[k][j];
      }
    }
  }

  // console.log(matrix);

  const carDict = {};
  for (let car of cars) {
    let [city, max, fee] = car.split(' ');
    if (city in carDict) {
      carDict[city].push([city, Number(max), Number(fee)]);
    } else {
      carDict[city] = [[city, Number(max), Number(fee)]];
    }
  }
  // console.log(carDict);

  for (let customer of customers) {
    let [from, to, weight] = customer.split(' ');
    let fromIdx = cities.indexOf(from);
    let toIdx = cities.indexOf(to);

    let cases = [];
    let res = ['a', Infinity];

    for (let i = 0; i < cities.length; i++) {
      if (matrix[fromIdx][i] != Infinity) {
        cases = cases.concat(carDict[cities[i]]);
      }
    }
    // console.log(cases);

    for (let i = 0; i < cases.length; i++) {
      if (Number(weight) > cases[i][1]) continue;

      let distance = 0;
      if (from != cases[i][0])
        distance += matrix[cities.indexOf(cases[i][0])][fromIdx];
      distance += matrix[fromIdx][toIdx];

      total = distance * cases[i][2];

      if (total < res[1]) res = [cases[i][0], total];
      else if (total == res[1]) {
        if (cases[i][0] < res[0]) res = [cases[i][0], total];
      }
    }

    answer.push(res[0]);
  }

  return answer;
}

console.log(
  solution(
    ['a', 'b', 'c'],
    ['a b 1', 'a c 1', 'b c 1'],
    ['a 100 10', 'b 300 20', 'c 50 4'],
    ['a b 100', 'a b 30', 'c a 250']
  )
);

console.log(
  solution(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    ['a b 1', 'a c 1', 'c d 3', 'b d 5', 'b e 6', 'd e 2', 'f g 8'],
    [
      'a 100 10',
      'a 200 15',
      'b 100 5',
      'c 20 2',
      'c 300 30',
      'd 200 20',
      'e 500 100',
      'f 500 50',
      'g 100 40',
    ],
    ['g f 200', 'c e 50', 'd a 500', 'a b 50']
  )
);
