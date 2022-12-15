let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
// king, queen, rook, bishop, night, pawn
// 1 1 2 2 2 8 -> 16
const count = [1,1,2,2,2,8];
const king = parseInt(input[0]);
const queen = parseInt(input[1]);
const rook = parseInt(input[2]);
const bishop = parseInt(input[3]);
const knight = parseInt(input[4]);
const pawn = parseInt(input[5]);

console.log("%d %d %d %d %d %d",count[0]-king, count[1]-queen, count[2]-rook, count[3]-bishop, count[4]-knight, count[5]-pawn);