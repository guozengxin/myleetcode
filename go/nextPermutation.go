package main

func nextPermutation(nums []int) {
	index := 0
	exIdx := 0
	for i := len(nums) - 1; i > 0; i -= 1 {
		if nums[i] <= nums[i-1] {
			continue
		}
		index = i - 1
		break
	}
	for i := len(nums) - 1; i > index; i -= 1 {
		if nums[i] > nums[index] {
			exIdx = i
			break
		}
	}
	if index != exIdx {
		nums[index], nums[exIdx] = nums[exIdx], nums[index]
	} else {
		index = -1
	}
	for i, j := len(nums)-1, index+1; i > j; i, j = i-1, j+1 {
		nums[i], nums[j] = nums[j], nums[i]
	}
}

func main() {
	nums := []int{3, 1, 1}
	nextPermutation(nums)
}
