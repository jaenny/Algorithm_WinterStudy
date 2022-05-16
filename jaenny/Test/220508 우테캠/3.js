let matrix = [];
let n = 0;
let m = 0;

function solution(board) {
  var answer = 0;
  matrix = board;
  n = matrix.length;
  m = matrix[0].length;

  // 세로
  for (let j = 0; j < m; j++) {
    let visit = createVisit(n, m);
    let res = bfs(0, j, 'down', visit);
    // console.log(j, res);
    if (answer < res) answer = res;
  }

  // 가로
  for (let i = 0; i < n; i++) {
    let visit = createVisit(n, m);
    let res = bfs(i, 0, 'right', visit);
    // console.log(i, res);
    if (answer < res) answer = res;
  }

  return answer;
}

function bfs(i, j, direction, visit) {
  const dy = [1, -1, 0, 0];
  const dx = [0, 0, 1, -1];

  let len = direction == 'down' ? visit.length : visit[0].length;

  let cnt = 0;
  let queue = [];

  if (direction == 'down') {
    for (let i = 0; i < len; i++) {
      if (visit[i][j] != 1) {
        visit[i][j] = 1;
        queue.push([i, j]);
        target = matrix[i][j];
        cnt += 1;

        while (queue) {
          if (queue.length == 0) break;
          // console.log(queue);
          let node = queue.shift();
          // console.log(node);
          let y = node[0];
          let x = node[1];

          for (let d = 0; d < 4; d++) {
            let ny = y + dy[d];
            let nx = x + dx[d];

            if (
              ny >= 0 &&
              ny < n &&
              nx >= 0 &&
              nx < m &&
              visit[ny][nx] != 1 &&
              matrix[ny][nx] == target
            ) {
              visit[ny][nx] = 1;
              cnt += 1;
              queue.push([ny, nx]);
            }
          }
        }
      }
    }
  } else {
    for (let j = 0; j < len; j++) {
      if (visit[i][j] != 1) {
        visit[i][j] = 1;
        queue.push([i, j]);
        target = matrix[i][j];
        cnt += 1;

        while (queue) {
          if (queue.length == 0) break;
          let node = queue.shift();
          let y = node[0];
          let x = node[1];

          for (let d = 0; d < 4; d++) {
            let ny = y + dy[d];
            let nx = x + dx[d];

            if (
              ny >= 0 &&
              ny < n &&
              nx >= 0 &&
              nx < m &&
              visit[ny][nx] != 1 &&
              matrix[ny][nx] == target
            ) {
              visit[ny][nx] = 1;
              cnt += 1;
              queue.push([ny, nx]);
            }
          }
        }
      }
    }
  }

  return cnt;
}

function createVisit(rows, cols) {
  let arr = new Array(rows);
  for (let i = 0; i < rows; i++) {
    arr[i] = new Array(cols);
  }
  return arr;
}

console.log(
  solution(['ABBBBC', 'AABAAC', 'BCDDAC', 'DCCDDE', 'DCCEDE', 'DDEEEB'])
);
console.log(solution(['DDCCC', 'DBBBC', 'DBABC', 'DBBBC', 'DDCCC']));
