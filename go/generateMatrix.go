package main

import "fmt"

func main() {
	//fmt.Printf("%+v\n", generateMatrix(3))
	res := generateMatrix(6)
	for i := 0; i < len(res); i += 1 {
		fmt.Printf("%+v\n", res[i])
	}
}

func generateMatrix(n int) [][]int {
	var result [][]int = make([][]int, n)
	for i := 0; i < n; i += 1 {
		result[i] = make([]int, n)
	}
	var i, j = 0, 0
	round := 0
	value := 1
	for {
		result[j][i] = value

		if j == round && i >= round && i < n-round-1 {
			i += 1
		} else if i == n-round-1 && j >= round && j < n-round-1 {
			j += 1
		} else if j == n-round-1 && i <= n-round-1 && i > round {
			i -= 1
		} else if i == round && j <= n-round-1 && j > round+1 {
			j -= 1
		} else if i == round && j == round+1 {
			i += 1
			round += 1
		}
		value += 1
		if value > n*n {
			break
		}
	}
	return result
}
