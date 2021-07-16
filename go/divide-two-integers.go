// https://leetcode-cn.com/problems/divide-two-integers/
package main

import (
	"fmt"
	"math"
)

func divide(dividend int, divisor int) int {
	if dividend == 0 {
		return 0

	}
	if divisor == 1 {
		return dividend
	}
	if divisor == -1 {
		if dividend > math.MinInt32 {
			return -dividend
		} else {
			return math.MaxInt32
		}
	}
	sign := 1
	if dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0 {
		sign = -1
	}
	if dividend < 0 {
		dividend = -dividend
	}
	if divisor < 0 {
		divisor = -divisor
	}

	return sign * div(dividend, divisor)
}

func div(a, b int) int {
	if a < b {
		return 0
	}
	count := 1
	bb := b
	for (bb + bb) <= a {
		count *= 2
		bb *= 2
	}
	return count + div(a-bb, b)
}

func main() {
	dividend := 100
	divisor := 10
	// dividend := -2147483648
	// divisor := -1
	fmt.Printf("%d\n", divide(dividend, divisor))
}
