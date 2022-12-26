package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	var hour, minute, time int
	fmt.Fscanln(reader, &hour, &minute)
	fmt.Fscanln(reader, &time)

	minute += time
	if minute >= 60 {
		hour += minute / 60
		minute %= 60
	}

	if hour >= 24 {
		hour %= 24
	}
	fmt.Println(hour, minute)
}
