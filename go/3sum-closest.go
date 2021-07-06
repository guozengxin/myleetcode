package main

import (
	"fmt"
	"sort"
)

func Abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func threeSumClosest(nums []int, target int) int {
	sort.Sort(sort.IntSlice(nums))
	fmt.Printf("nums: %+v\n", nums)
	var result = 0
	var set = false
	for i := 0; i < len(nums)-2; i += 1 {
		j, k := i+1, len(nums)-1
		for j < k {
			sum := nums[i] + nums[j] + nums[k]
			fmt.Printf("%d %d %d -- %d\n", i, j, k, sum)
			if sum < target {
				j += 1
			} else if sum > target {
				k -= 1
			}
			if !set || Abs(sum-target) < Abs(result-target) {
				result = sum
				set = true
			}
			if result == target {
				break
			}
		}
	}
	return result
}

func main() {
	// nums := []int{-1, 2, 1, -4}
	nums := []int{0, 1, 2}
	target := 3
	result := threeSumClosest(nums, target)
	fmt.Printf("result is: %d\n", result)
}
