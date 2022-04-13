package main

func main() {
	return
}

func solution(nums []int) int {
	answer := 0

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			for k := j + 1; k < len(nums); k++ {
				if isPrime(nums[i] + nums[j] + nums[k]) {
					answer += 1
				}
			}
		}
	}
	return answer
}

func isPrime(num int) bool {
	if num <= 2 {
		return false
	}
	for i := 2; i < num; i++ {
		if (num % i) == 0 {
			return false
		}
	}
	return true
}
