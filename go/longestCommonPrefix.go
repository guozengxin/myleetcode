package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	var index = 0
	var res = ""
	for true {
		var ch byte
		for _, str := range strs {
			if len(str) < index+1 {
				ch = 0
				break
			}
			if ch == 0 {
				ch = str[index]
			} else if ch == str[index] {
				continue
			} else {
				ch = 0
				break
			}
		}
		if ch == 0 {
			break
		}
		res += string([]byte{ch})
		index += 1
	}
	return res
}

func main() {
	var strs = []string{
		"ower",
		"ag",
		"ow",
	}
	fmt.Printf("%s\n", longestCommonPrefix(strs))
}
