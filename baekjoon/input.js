let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

console.log(input)

let a = input[0]
let b = input[1]

console.log("a : ", a)
console.log("b : ", b)

console.log(Number(a) + Number(b))
console.log(parseInt(a,10)+parseInt(b,10))
