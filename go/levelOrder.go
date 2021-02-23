package main

import (
	"container/list"
	"fmt"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	var res [][]int
	if root == nil {
		return res
	}
	l := list.New()
	l.PushBack(root)
	for l.Len() > 0 {
		arr := []int{}
		for nowLen := l.Len(); nowLen > 0; nowLen-- {
			nodeV := l.Front()
			node := nodeV.Value.(*TreeNode)
			arr = append(arr, node.Val)

			l.Remove(nodeV)
			if node.Left != nil {
				l.PushBack(node.Left)
			}
			if node.Right != nil {
				l.PushBack(node.Right)
			}
		}
		res = append(res, arr)
	}
	return res
}

func main() {
	var root *TreeNode = &TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}
	root.Left = &TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}
	root.Right = &TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}
	root.Right.Left = &TreeNode{
		Val:   4,
		Left:  nil,
		Right: nil,
	}

	res := levelOrder(root)
	fmt.Printf("%+v\n", res)
}
