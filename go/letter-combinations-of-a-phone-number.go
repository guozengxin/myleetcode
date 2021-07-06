package main

import "fmt"

func letterCombinations(digits string) []string {
	var digitMap = map[byte][]byte{
		'2': []byte{'a', 'b', 'c'},
		'3': []byte{'d', 'e', 'f'},
		'4': []byte{'g', 'h', 'i'},
		'5': []byte{'j', 'k', 'l'},
		'6': []byte{'m', 'n', 'o'},
		'7': []byte{'p', 'q', 'r', 's'},
		'8': []byte{'t', 'u', 'v'},
		'9': []byte{'w', 'x', 'y', 'z'},
	}

	resultList := []string{}
	if len(digits) == 0 {
		return resultList
	}

	resultBytesList := [][]byte{}
	for _, ch := range digitMap[digits[0]] {
		resultBytesList = append(resultBytesList, []byte{ch})
	}
	for _, digit := range digits[1:len(digits)] {
		newResultBytesList := [][]byte{}
		for _, prefix := range resultBytesList {
			for _, ch := range digitMap[byte(digit)] {
				newPrefix := make([]byte, len(prefix))
				copy(newPrefix, prefix)
				bytes := append(newPrefix, ch)
				newResultBytesList = append(newResultBytesList, bytes)
			}
		}
		resultBytesList = newResultBytesList
	}
	for _, resultBytes := range resultBytesList {
		resultList = append(resultList, string(resultBytes))
	}
	return resultList
}

func main() {
	//digits := "23"
	//digits := "2"
	digits := "234"
	fmt.Printf("%+v\n", letterCombinations(digits))
}
