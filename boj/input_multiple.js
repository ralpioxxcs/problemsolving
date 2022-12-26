let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n');

console.log(input)

console.log(input.length)
for (let i = 1; i < input.length; i++) {
  let nums = input[i].split(' ');
  console.log("num 1:",nums[0]);
  console.log("num 2:",nums[1]);
}


