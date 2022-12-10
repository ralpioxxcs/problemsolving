package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	curIdx int
	res    []rune
	maxLen = 80
	aBin   = []rune{'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'}
	bBin   = []rune{'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'}
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input := scanner.Text()
	binarys := strings.Split(input, " ")

	aInput := []rune(binarys[0]) // 10011
	bInput := []rune(binarys[1]) //   101

	var longer int // 두 배열중 더 긴 배열의 길이
	if len(aInput)-len(bInput) > 0 {
		longer = len(aInput)
	} else {
		longer = len(bInput)
	}

	for i, j := len(aBin)-1, len(aInput)-1; j >= 0; i, j = i-1, j-1 {
		aBin[i] = aInput[j]
	}
	for i, j := len(bBin)-1, len(bInput)-1; j >= 0; i, j = i-1, j-1 {
		bBin[i] = bInput[j]
	}
	aBin = aBin[maxLen-longer:]
	bBin = bBin[maxLen-longer:]

	curIdx = len(aBin) - 1
	adder(aBin[curIdx], bBin[curIdx], '0')

	var resultStr string
	if len(res) > 1 {
		count := len(res)
		resultStr = strings.TrimLeftFunc(string(res), func(r rune) bool {
			count -= 1
			if r == '0' && count > 0 {
				return true
			} else {
				return false
			}
		})
	} else {
		resultStr = string(res)
	}

	fmt.Println(resultStr)
	return
}

func adder(a_, b_, ci_ rune) (s_, co_ rune) {
	if curIdx == 0 {
		s_, co_ = ' ', ' '
		a, _ := strconv.ParseInt(string(a_), 2, 0)
		b, _ := strconv.ParseInt(string(b_), 2, 0)
		ci, _ := strconv.ParseInt(string(ci_), 2, 0)
		s := a ^ b ^ ci
		co := (a & b) ^ ci&(a^b)
		s_ = []rune(strconv.FormatInt(int64(s), 2))[0]
		co_ = []rune(strconv.FormatInt(int64(co), 2))[0]
		res = append([]rune{s_}, res...)
		res = append([]rune{co_}, res...)
		if co != 0 {
		}
		return
	}
	a, _ := strconv.ParseInt(string(a_), 2, 0)
	b, _ := strconv.ParseInt(string(b_), 2, 0)
	ci, _ := strconv.ParseInt(string(ci_), 2, 0)
	s := a ^ b ^ ci
	co := (a & b) ^ ci&(a^b)
	s_ = []rune(strconv.FormatInt(int64(s), 2))[0]
	co_ = []rune(strconv.FormatInt(int64(co), 2))[0]
	res = append([]rune{s_}, res...)
	curIdx -= 1

	return adder(aBin[curIdx], bBin[curIdx], co_)
}
