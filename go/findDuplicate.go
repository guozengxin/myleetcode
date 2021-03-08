package main

import "fmt"

func main() {
	// nums := []int{1, 3, 4, 2, 2}
	// nums := []int{3, 1, 3, 4, 2}
	// nums := []int{1, 1}
	nums := []int{1, 1, 2}
	fmt.Printf("%+v\n", findDuplicate(nums))
}

func findDuplicate(nums []int) int {
	m := map[int]bool{}
	for _, n := range nums {
		if m[n] {
			return n
		}
		m[n] = true
	}
	return -1
}
