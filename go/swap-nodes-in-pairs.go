// https://leetcode-cn.com/problems/swap-nodes-in-pairs/
package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	topNode := &ListNode{0, head}
	preNode := topNode
	firstNode := topNode.Next
	var secondNode *ListNode
	if firstNode != nil {
		secondNode = firstNode.Next
	}
	for firstNode != nil && secondNode != nil {
		preNode.Next = secondNode
		firstNode.Next = secondNode.Next
		secondNode.Next = firstNode

		// fmt.Printf("%d %d %d\n", preNode.Val, firstNode.Val, secondNode.Val)

		preNode = firstNode
		firstNode = preNode.Next
		if firstNode != nil {
			secondNode = firstNode.Next
		}
	}
	return topNode.Next
}

func main() {
	head := &ListNode{1, nil}
	head.Next = &ListNode{2, nil}
	head.Next.Next = &ListNode{3, nil}
	head.Next.Next.Next = &ListNode{4, nil}

	result := swapPairs(head)
	for result != nil {
		fmt.Printf("%d - ", result.Val)
		result = result.Next
	}
}
