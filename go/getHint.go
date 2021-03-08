package main

import "fmt"

func main() {
	//secret := "1807"
	//guess := "7810"
	secret := "1123"
	guess := "0111"
	fmt.Printf("%s\n", getHint(secret, guess))
}

func minInt(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func getHint(secret string, guess string) string {
	secretArr := []byte(secret)
	guessArr := []byte(guess)
	aCount := 0
	bCount := 0
	secretMap := make(map[byte]int)
	guessMap := make(map[byte]int)
	for i := 0; i < len(secretArr); i += 1 {
		fmt.Printf("%s, %s\n", string(secretArr[i]), string(guessArr[i]))
		if secretArr[i] == guessArr[i] {
			aCount += 1
		} else {
			secretMap[secretArr[i]] += 1
			guessMap[guessArr[i]] += 1
		}
	}
	for key, _ := range secretMap {
		bCount += minInt(secretMap[key], guessMap[key])
	}
	return fmt.Sprintf("%dA%dB", aCount, bCount)
}
