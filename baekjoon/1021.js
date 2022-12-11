let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

fl = input[0].split(' ');
sl = input[1].split(' ');

n = fl[0]; // <= 50
m = fl[1]; // <= n
extractNum = sl;

let deque = []; // empty array
for (let i = 0; i < n; i++) {
  deque.push(i + 1);
}

let count = 0;
// 1 2 3 4 5 6 7 8 9 10 moveleft
// 2 3 4 5 6 7 8 9 10 1
// 3 4 5 6 7 8 9 10 1 moveright
// 1 3 4 5 6 7 8 9 10 moveright
// 10 1 3 4 5 6 7 8 9 moveright
// 9 10 1 3 4 5 6 7 8 moveright
extractNum.forEach((number) => {
  const idx = deque.indexOf(parseInt(number, 10));
  if (idx == 0) {
    deque.splice(0, 1);
  } else if ((idx + 1) <= Math.round(deque.length / 2)) {
    for (let i = 0; i < idx; i++) {
      count += 1;
      moveLeft();
    }
    deque.splice(0, 1);
  } else {
    for (let i = 0; i < (deque.length - (idx)); i++) {
      count += 1;
      moveRight();
    }
    deque.splice(0, 1);
  }
});

console.log(count);

function moveLeft() {
  deque.push(deque[0]);
  deque.splice(0, 1);
  console.debug("move left");
  console.debug(deque);
}
function moveRight() {
  deque.splice(0, 0, deque[deque.length - 1]);
  deque.splice(deque.length - 1, 1);
  console.debug("move right");
  console.debug(deque);
}
