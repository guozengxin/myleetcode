// https://leetcode-cn.com/problems/merge-k-sorted-lists/
package main

import (
	"container/heap"
	"fmt"
)

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

type MinHeap []*ListNode

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	// 由于是最大堆，所以使用大于号
	return h[i].Val < h[j].Val
}

func (h *MinHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(*ListNode))
}

func (h *MinHeap) Pop() interface{} {
	res := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return res
}

func mergeKLists(lists []*ListNode) *ListNode {
	mh := MinHeap{}
	for _, l := range lists {
		if l != nil {
			mh = append(mh, l)
		}
	}
	heap.Init(&mh)
	var result = &ListNode{}
	p := result
	for mh.Len() > 0 {
		head := heap.Pop(&mh).(*ListNode)
		p.Next = head
		p = p.Next
		if head.Next != nil {
			heap.Push(&mh, head.Next)
		}
	}
	return result.Next
}

func main() {
	list := []*ListNode{}
	l1 := &ListNode{1, nil}
	l1.Next = &ListNode{4, nil}
	l1.Next.Next = &ListNode{5, nil}

	l2 := &ListNode{1, nil}
	l2.Next = &ListNode{3, nil}
	l2.Next.Next = &ListNode{4, nil}

	l3 := &ListNode{2, nil}
	l3.Next = &ListNode{6, nil}

	l1 = nil
	l2 = nil
	list = append(list, l1, l2)
	fmt.Printf("%d\n", len(list))

	// list = append(list, l1, l2, l3)

	result := mergeKLists(list)
	for result != nil {
		fmt.Printf("%+v - ", result.Val)
		result = result.Next
	}
	fmt.Println()
}
