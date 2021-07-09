// https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	top := &ListNode{0, head}
	length := 0
	for p := head; p != nil; p = p.Next {
		length += 1
	}
	lastTop := top
	for i := 0; i < length/k; i += 1 {
		fmt.Printf("i: %v\n", i)
		p := head.Next
		for j := 0; j < k-1; j += 1 {
			fmt.Printf("j: %v p.Val: %v\n", j, p.Val)
			next := p.Next
			p.Next = lastTop.Next
			lastTop.Next = p
			p = next
		}
		lastTop = head
		head.Next = p
		head = p
	}
	return top.Next
}

func main() {
	l := &ListNode{1, nil}
	/*
		l.Next = &ListNode{2, nil}
		l.Next.Next = &ListNode{3, nil}
		l.Next.Next.Next = &ListNode{4, nil}
		l.Next.Next.Next.Next = &ListNode{5, nil}
	*/

	result := reverseKGroup(l, 0)
	for result != nil {
		fmt.Printf("%+v - ", result.Val)
		result = result.Next
	}
	fmt.Println()
}
