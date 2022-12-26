## python
```python
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
```


## golang
```go
reader := bufio.NewReader(os.Stdin)
fmt.Fscanln(reader, &tc); // testcase
for i:=0; i < n; i++ {
  fmt.Fscanln(reader, &a, &b)
  ...
}
```


## node.js
```js
const path = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = require("fs").readFileSync(path).toString().trim().split("\n");
```
