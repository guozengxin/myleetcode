package main

import "fmt"

func main() {
	fmt.Printf("%d\n", calRes(37))
	fmt.Printf("2 %v\n", isHappy(2))
	fmt.Printf("19 %v\n", isHappy(19))
}

func calRes(n int) int {
	res := 0
	for n > 0 {
		res += (n % 10) * (n % 10)
		n = n / 10
	}
	return res
}

func isHappy(n int) bool {
	mm := map[int]bool{}
	mm[n] = true
	res := n
	for {
		res = calRes(res)
		if res == 1 {
			return true
		} else if mm[res] {
			return false
		}
		mm[res] = true
	}
	return false
}
