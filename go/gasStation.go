package main

import "fmt"

func main() {
	//gas := []int{1, 2, 3, 4, 5}
	//cost := []int{3, 4, 5, 1, 2}
	//gas := []int{2, 3, 4}
	//cost := []int{3, 4, 3}
	gas := []int{5, 1, 2, 3, 4}
	cost := []int{4, 4, 1, 5, 1}
	fmt.Printf("%d\n", canCompleteCircuit(gas, cost))
}

func canCompleteCircuit(gas []int, cost []int) int {
	count := len(gas)
	start := 0
	nowGas := 0
	for i := 0; i < count*2; i += 1 {
		nowGas += gas[i%count]
		if nowGas >= cost[i%count] {
			nowGas -= cost[i%count]
		} else if nowGas < cost[i%count] {
			start = i + 1
			nowGas = 0
		}
		if start >= count {
			return -1
		}
		if i > start+count {
			return start
		}
	}
	if start < count {
		return start
	}
	return -1
}
