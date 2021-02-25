package main

import (
	"fmt"
)

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Printf("%v\n", trap(height))
}

func maxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func minInt(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func trap(height []int) int {

	var left = make([]int, len(height))
	var right = make([]int, len(height))
	for i := 1; i < len(height); i += 1 {
		left[i] = maxInt(left[i-1], height[i-1])
	}
	for j := len(height) - 2; j >= 0; j -= 1 {
		right[j] = maxInt(right[j+1], height[j+1])
	}

	water := 0
	for i := 1; i < len(height)-1; i += 1 {
		level := minInt(left[i], right[i])
		if level > height[i] {
			water += level - height[i]
		}
	}
	return water
}
