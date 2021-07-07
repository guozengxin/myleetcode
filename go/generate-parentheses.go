// https://leetcode-cn.com/problems/generate-parentheses/
package main

import "fmt"

func generateParenthesis(n int) []string {
	if n == 1 {
		return []string{"()"}
	}
	result := generateParenthesis(n - 1)
	resultMap := make(map[string]struct{})
	for _, s := range result {
		for i := range s {
			newstr := s[0:i] + "()" + s[i:]
			resultMap[newstr] = struct{}{}
		}
	}
	result = []string{}
	for key, _ := range resultMap {
		result = append(result, key)
	}
	return result
}

func main() {
	n := 4
	fmt.Printf("%+v\n", generateParenthesis(n))
}
