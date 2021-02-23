package main

import "fmt"

func searchInsert(nums []int, target int) int {
	index := -1
	for i, n := range nums {
		if target > n {
			continue
		} else if target <= n {
			index = i
			break
		}
	}
	if index == -1 {
		index = len(nums)
	}
	return index
}

func main() {
	nums, target := []int{3, 5, 6}, 1
	fmt.Printf("%d\n", searchInsert(nums, target))
	nums, target = []int{1, 2, 3, 8}, 20
	fmt.Printf("%d\n", searchInsert(nums, target))
	nums, target = []int{1, 2, 3, 8, 20}, 20
	fmt.Printf("%d\n", searchInsert(nums, target))
	nums, target = []int{1, 2, 3, 8, 20}, 1
	fmt.Printf("%d\n", searchInsert(nums, target))
}
