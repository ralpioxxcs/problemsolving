package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	maps := make(map[int]int)
	for scanner.Scan() {
		txt := scanner.Text()
		if txt == "" {
			break
		}
		num, _ := strconv.Atoi(txt)
		maps[int(num)%42] = 1
	}
	fmt.Println(len(maps))
}
