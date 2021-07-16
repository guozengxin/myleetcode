// https://leetcode-cn.com/problems/remove-element/
package main

import "fmt"

func removeElement(nums []int, val int) int {
	i := 0
	j := len(nums) - 1
	for i <= j {
		if nums[i] == val {
			nums[i] = nums[j]
			j--
		} else {
			i++
		}
	}
	return i
}

func main() {
	// nums := []int{3, 2, 2, 3}
	// nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	nums := []int{1}
	val := 2
	fmt.Printf("%d ", removeElement(nums, val))
	fmt.Printf("%+v\n", nums)
}
