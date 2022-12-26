package main

import (
	"bufio"
	"fmt"
	"os"
)

type bulk struct {
	tall   int
	weight int
	rank   int
}

var (
	tc       int
	bulkList []bulk
)

func main() {
	input()
	solve()
	for _, v := range bulkList {
		fmt.Println(v.rank)
	}
}

func input() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Fscanln(reader, &tc)
	for i := 0; i < tc; i++ {
		var x, y int
		fmt.Fscanln(reader, &x, &y)
		bulkList = append(bulkList, bulk{x, y, 0})
	}
}

func solve() {
	for i := 0; i < len(bulkList); i++ {
		higher := 0
		for j := 0; j < len(bulkList); j++ {
			if i == j {
				continue
			}
			if bulkList[i].tall < bulkList[j].tall && bulkList[i].weight < bulkList[j].weight {
				higher += 1
			}
		}
		bulkList[i].rank = higher + 1
	}
}
