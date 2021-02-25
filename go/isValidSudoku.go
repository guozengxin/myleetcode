package main

import "fmt"

func main() {
	/*
		board := [][]byte{
			[]byte{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
			[]byte{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
			[]byte{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
			[]byte{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
			[]byte{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
			[]byte{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
			[]byte{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
			[]byte{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
			[]byte{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
		}
	*/
	board := [][]byte{
		{'8', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}
	fmt.Printf("%v\n", isValidSudoku(board))
}

func isValidSudoku(board [][]byte) bool {
	for i := 0; i < 9; i += 1 {
		m := map[byte]bool{}
		for j := 0; j < 9; j += 1 {
			if board[i][j] == '.' {
				continue
			} else if m[board[i][j]] {
				return false
			} else {
				m[board[i][j]] = true
			}
		}
	}

	for j := 0; j < 9; j += 1 {
		m := map[byte]bool{}
		for i := 0; i < 9; i += 1 {
			if board[i][j] == '.' {
				continue
			} else if m[board[i][j]] {
				return false
			} else {
				m[board[i][j]] = true
			}
		}
	}

	for ii := 3; ii <= 9; ii += 3 {
		for jj := 3; jj <= 9; jj += 3 {
			m := map[byte]bool{}
			for i := ii - 3; i < ii; i += 1 {
				for j := jj - 3; j < jj; j += 1 {
					if board[i][j] == '.' {
						continue
					} else if m[board[i][j]] {
						return false
					} else {
						m[board[i][j]] = true
					}
				}
			}

		}
	}

	return true
}
