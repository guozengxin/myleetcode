package main

import "fmt"

func removeDuplicates(nums []int) int {

	var i = 0
	for index, n := range nums {
		if index == 0 {
			i += 1
			continue
		}
		if n != nums[index-1] {
			nums[i] = n
			i += 1
		}
	}
	return i
}

func main() {
	var nums = []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Printf("%+v\n", removeDuplicates(nums))
}
