// https://leetcode-cn.com/problems/implement-strstr/
package main

import "fmt"

func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}
	for i := 0; i <= len(haystack)-len(needle); i += 1 {
		j := 0
		for ; j < len(needle); j += 1 {
			if haystack[i+j] != needle[j] {
				break
			}
		}
		if j == len(needle) {
			return i
		}
	}
	return -1
}

func main() {
	haystack := "aabbccc"
	needle := "abc"
	fmt.Printf("%d\n", strStr(haystack, needle))
}
