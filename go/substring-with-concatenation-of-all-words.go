// https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
package main

import "fmt"

func copyMap(m map[string]int) map[string]int {
	copyMap := make(map[string]int, len(m))
	for k, v := range m {
		copyMap[k] = v
	}
	return copyMap
}

func findSubstring(s string, words []string) []int {
	result := []int{}
	if len(words) == 0 {
		return result
	}
	singleLen := len(words[0])
	totalLen := singleLen * len(words)
	wordsMap := map[string]int{}
	for _, w := range words {
		wordsMap[w] += 1
	}
	failedIndexMap := map[int]struct{}{}
	for i := 0; i <= len(s)-totalLen; i += 1 {
		if _, found := failedIndexMap[i]; found {
			continue
		}
		copyWordsMap := copyMap(wordsMap)
		foundWords := 0
		for j := i; j < i+totalLen; j += singleLen {
			w := s[j : j+singleLen]
			if value, found := copyWordsMap[w]; found {
				if value > 0 {
					copyWordsMap[w] -= 1
					foundWords += 1
				} else {
					break
				}
			} else {
				if j > i {
					failedIndexMap[j] = struct{}{}
				}
			}
		}
		fmt.Printf("i: %d, foundWords: %d words: %d\n", i, foundWords, len(words))
		if foundWords == len(words) {
			result = append(result, i)
		}

	}
	return result
}

func main() {
	/*
		s := "barfoothefoobarman"
		words := []string{"foo", "bar"}
	*/
	s := "barfoofoobarthefoobarman"
	words := []string{"bar", "foo", "the"}
	fmt.Printf("%+v\n", findSubstring(s, words))
}
