// https://leetcode-cn.com/problems/4sum/
package main

import (
	"fmt"
	"sort"
)

func sliceEqual(s1, s2 []int) bool {
	if len(s1) != len(s2) {
		return false
	}
	for i := 0; i < len(s1); i += 1 {
		if s1[i] != s2[i] {
			return false
		}
	}
	return true
}

func fourSum(nums []int, target int) [][]int {
	sort.Sort(sort.IntSlice(nums))
	fmt.Printf("%+v\n", nums)
	count := len(nums)
	lastResult := make([]int, 0)
	resultList := make([][]int, 0)
	for i1 := 0; i1 < count; i1 += 1 {
		if i1 > 0 && nums[i1] == nums[i1-1] {
			continue
		}
		for i2 := i1 + 1; i2 < count; i2 += 1 {
			if i2 > i1+1 && nums[i2] == nums[i2-1] {
				continue
			}
			if nums[i1]+nums[i2]+nums[count-1]+nums[count-2] < target {
				continue
			}
			j, k := i2+1, count-1
			for j < k {
				sum := nums[i1] + nums[i2] + nums[j] + nums[k]
				fmt.Printf("%d %d %d %d -- %d\n", nums[i1], nums[i2], nums[j], nums[k], sum)
				if sum < target {
					j += 1
				} else if sum > target {
					k -= 1
				} else {
					// 这里可以通过比较和移动j, k位置，避免lastResult这个比较操作，可以省点空间和时间
					s := []int{nums[i1], nums[i2], nums[j], nums[k]}
					if !sliceEqual(s, lastResult) {
						resultList = append(resultList, s)
						lastResult = s
					}
					j += 1
					k -= 1
				}
			}
		}
	}
	return resultList
}

func main() {
	// nums := []int{1, 0, -1, 0, -2, 2}
	// target := 0
	// nums := []int{2, 2, 2, 2, 2}
	// target := 7
	// nums := []int{-3, -2, -1, 0, 0, 1, 2, 3}
	// target := 0
	// nums := []int{-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5}
	// target := 0
	nums := []int{2, 0, 3, 0, 1, 2, 4}
	target := 7

	fmt.Printf("%+v\n", fourSum(nums, target))
}
