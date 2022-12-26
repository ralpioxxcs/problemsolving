package main

import (
	"fmt"
	"strconv"
)

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)
	aS, bS := strconv.FormatInt(int64(a), 10), strconv.FormatInt(int64(b), 10)
	ras, rbs := reverse(aS), reverse(bS)
	if ras > rbs {
		fmt.Println(ras)
	} else {
		fmt.Println(rbs)
	}
}

func reverse(input string) string {
	runes := []rune(input)
	reversed := []rune{}
	for i := len(runes) - 1; i >= 0; i = i - 1 {
		reversed = append(reversed, runes[i])
	}
	return string(reversed)
}
