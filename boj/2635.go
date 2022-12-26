package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d\n", &n)

	max, nums := solve(n)
	fmt.Println(max)
	for _, v := range nums {
		fmt.Printf("%d ", v)
	}
}

func solve(n int) (max int, nums []int) {
	max = 0
	for i := n / 2; i <= n; i++ {
		numbers := []int{n, i}
		for {
			next := numbers[len(numbers)-2] - numbers[len(numbers)-1]
			if next < 0 {
				break
			} else {
				numbers = append(numbers, next)
			}
		}
		if len(numbers) > max {
			max = len(numbers)
			nums = numbers
		}
	}
	return
}
