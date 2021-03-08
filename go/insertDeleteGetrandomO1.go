package main

import (
	"fmt"
	"math/rand"
)

type RandomizedSet struct {
	data map[int]int
	arr  []int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{
		data: make(map[int]int),
		arr:  make([]int, 0),
	}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.data[val]; ok {
		return false
	}
	this.arr = append(this.arr, val)
	this.data[val] = len(this.arr) - 1

	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.data[val]; !ok {
		return false
	}
	index := this.data[val]
	this.arr[index] = this.arr[len(this.arr)-1]
	this.data[this.arr[index]] = index
	delete(this.data, val)
	this.arr = this.arr[:len(this.arr)-1]
	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	if len(this.arr) == 0 {
		return -1
	}
	index := rand.Intn(len(this.arr))
	return this.arr[index]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */

func main() {
	val := 1
	obj := Constructor()
	param_1 := obj.Insert(val)
	param_2 := obj.Remove(val)
	obj.Insert(2)
	param_3 := obj.GetRandom()
	fmt.Printf("%+v, %+v %+v \n", param_1, param_2, param_3)
}
