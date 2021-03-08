package main

import "fmt"

func main() {
	//nums := []int{1, 2, 3, 1}
	//nums := []int{2, 3, 2}
	//nums := []int{0}
	//nums := []int{}
	nums := []int{1, 1, 1, 1, 1}
	fmt.Printf("%+v\n", rob(nums))
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	return maxInt(robHelper(nums[1:]), robHelper(nums[:len(nums)-1]))
}

func robHelper(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	var res = make([]int, len(nums))
	for i, num := range nums {
		if i == 0 {
			res[i] = num
		} else if i == 1 {
			res[i] = maxInt(nums[0], nums[1])
		} else {
			res[i] = maxInt(res[i-1], res[i-2]+num)
		}
	}
	return res[len(nums)-1]
}
