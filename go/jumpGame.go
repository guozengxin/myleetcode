package main

import "fmt"

func main() {
	//nums := []int{2, 3, 1, 1, 4}
	nums := []int{3, 2, 1, 0, 4}
	fmt.Printf("%+v\n", canJump(nums))
}

func maxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func canJump(nums []int) bool {
	var k = 0
	for i, n := range nums {
		if i > k {
			return false
		}
		k = maxInt(k, i+n)
	}
	return true
}
