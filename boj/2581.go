package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	m, n int64
	sum  int = 0
	min  int = math.MaxInt
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	m, _ = strconv.ParseInt(scanner.Text(), 10, 0)
	scanner.Scan()
	n, _ = strconv.ParseInt(scanner.Text(), 10, 0)

	count := 0
	for i := m; i <= n; i += 1 {
		if isPrime(int(i)) {
			sum += int(i)
			min = int(math.Min(float64(i), float64(min)))
			count += 1
		}
	}

	if count == 0 {
		fmt.Println("-1")
	} else {
		fmt.Println(sum)
		fmt.Println(min)
	}
}

func isPrime(v int) bool {
	if v == 1 {
		return false
	}
	for i := 2; i < v; i += 1 {
		if v%i == 0 {
			return false
		}
	}
	return true
}
