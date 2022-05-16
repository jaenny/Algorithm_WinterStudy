// 상수만 가지고 1부터 10까지 더하기

const a = 1;

function plus(num) {
  if (num === 10) {
    console.log(num);
    return;
  }
  return plus(num + 1);
}

plus(a);

// 배열에서 0을 다 오른쪽으로 보내기

const arr = [1, 0, 2, 0, 3, 0];

for (let i = 0; i < arr.length; i++) {
  for (let j = i + 1; j < arr.length; j++) {
    if (arr[i] === 0 && arr[j] !== 0) {
      temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
      break;
    }
  }
}
console.log(arr);

// 팩토리얼
function factorial(num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(4));

// 피보나치
// 재귀를 이용한 피보나치 수열 - 시간복잡도 : O(2^n)
function Fibo1(num) {
  if (num < 2) {
    return num;
  }

  return Fibo1(num - 1) + Fibo1(num - 2);
}
console.log(Fibo1(7));

// 동적계획법을 이용한 피보나치 수열 - 시간복잡도 : O(N)
const n = 7;
const dp = new Array(n + 1);
dp[0] = 0;
dp[1] = 1;

for (let i = 2; i <= n; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
}
console.log(dp);

// 10번 동안 1~10까지 랜덤한 숫자를 출력하여 중복된 숫자가 있을 시 true 리턴
const visit = new Array(11);
for (let i = 0; i < 10; i++) {
  let randomNum = Math.floor(Math.random() * 10) + 1;
  console.log(randomNum);
  if (visit[randomNum]) {
    console.log(false);
    break;
  }
  visit[randomNum] = true;
}

// 정렬
// 선택정렬 - 들어갈 자리는 정해져 있고, 어떤 수를 넣을 지 선택하는 정렬 방법
const arr1 = [2, 5, 4, 3, 1];
for (let i = 0; i < arr1.length; i++) {
  _minNum = arr1[i];
  _minNumIndex = i;
  for (let j = i + 1; j < arr1.length; j++) {
    if (arr1[j] < _minNum) {
      _minNum = arr1[j];
      _minNumIndex = j;
    }
  }

  [arr1[i], arr1[_minNumIndex]] = [arr1[_minNumIndex], arr1[i]];
}
console.log('선택 정렬', arr1);

// 버블정렬 - 인접한 두 수를 SWAP하는 방식으로 정렬하는 방법
const arr2 = [2, 5, 4, 3, 1];
for (let i = arr2.length - 1; i >= 0; i--) {
  for (let j = 0; j < i; j++) {
    if (arr2[j] > arr2[j + 1]) {
      [arr2[j], arr2[j + 1]] = [arr2[j + 1], arr2[j]];
    }
  }
}
console.log('버블 정렬', arr2);

// 삽입정렬 - 수는 정해져 있고, 어느 위치에 삽입할 지 고르는 것
const arr3 = [2, 5, 4, 3, 1];
for (let i = 1; i < arr3.length; i++) {
  let insertNum = arr3[i];
  let left = i - 1;

  while (left >= 0 && arr3[left] > insertNum) {
    arr3[left + 1] = arr3[left];
    left--;
  }
  arr3[left + 1] = insertNum;
}
console.log('삽입 정렬', arr3);

// 퀵소트
function quickSort(array) {
  if (array.length < 2) {
    return array;
  }
  const pivot = [array[0]];
  const left = [];
  const right = [];
  for (let i = 1; i < array.length; i++) {
    if (array[i] < pivot) {
      left.push(array[i]);
    } else if (array[i] > pivot) {
      right.push(array[i]);
    } else {
      pivot.push(array[i]);
    }
  }
  console.log(`left: ${left}, pivot: ${pivot}, right: ${right}`);
  return quickSort(left).concat(pivot, quickSort(right));
}
const sorted = quickSort([5, 3, 7, 1, 9]);
console.log('퀵 정렬', sorted);

// 머지 소트
function mergeSort(array) {
  if (array.length < 2) {
    return array;
  }

  const mid = Math.floor(array.length / 2);
  const left = array.slice(0, mid);
  const right = array.slice(mid);

  return merge(mergeSort(left), mergeSort(right));

  function merge(left, right) {
    const resultArray = [];

    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        resultArray.push(left[leftIndex]);
        leftIndex++;
      } else {
        resultArray.push(right[rightIndex]);
        rightIndex++;
      }
    }
    return resultArray.concat(left.slice(leftIndex), right.slice(rightIndex));
  }
}
console.log('머지 정렬', mergeSort([5, 4, 3, 2, 1]));

// 주어진 두 문자가 아나그램인지 확인
function anagrams(stringA, stringB) {
  return cleanString(stringA) === cleanString(stringB);
}

function cleanString(str) {
  return (str = str.replace(/\s/g, '').toLowerCase().split('').sort().join(''));
}

console.log('anagrams', anagrams('h at', 't a h'));

// 팰린드롬
function palindrome(str) {
  const reversed = str.split('').reverse().join('');
  return reversed === str ? true : false;
}
console.log('팰린드롬', palindrome('abba'));

// 고유한 문자인지 확인
const charVisit = [];
const str = 'abc cde';

function isUniqueChar(str) {
  for (let i = 0; i < str.length; i++) {
    if (charVisit.includes(str[i])) {
      return false;
    } else {
      charVisit.push(str[i]);
    }
  }
}

console.log('고유한 문자인지 확인', isUniqueChar(str));

// 최소공배수, 최소공약수
function solution(num1, num2) {
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  const lcm = (a, b) => (a * b) / gcd(a, b);
  return [gcd(num1, num2), lcm(num1, num2)];
}

// 하노이의 탑
function solution(n) {
  const answer = [];

  function hanoi(n, from, to) {
    const by = 6 - from - to;

    if (n === 1) {
      answer.push([from, to]);
    } else {
      hanoi(n - 1, from, by);
      answer.push([from, to]);
      hanoi(n - 1, by, to);
    }
  }
  hanoi(n, 1, 3);

  return answer;
}

console.log(solution(2));
