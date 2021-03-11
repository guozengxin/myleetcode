package main

import "fmt"

// Definition for a binary tree node.

func main() {
	root := &TreeNode{5, nil, nil}
	root.Left = &TreeNode{3, nil, nil}
	root.Right = &TreeNode{6, nil, nil}
	root.Left.Left = &TreeNode{2, nil, nil}
	root.Left.Right = &TreeNode{4, nil, nil}
	root.Left.Left.Left = &TreeNode{1, nil, nil}
	root.Left.Right.Right = &TreeNode{8, nil, nil}
	fmt.Printf("%+v\n", zigzagLevelOrder(root))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	result := [][]int{}
	if root == nil {
		return result
	}
	arr1 := []*TreeNode{}
	arr2 := []*TreeNode{}
	o := true
	arr1 = append(arr1, root)
	for len(arr1) > 0 {
		level := []int{}
		for i := range arr1 {
			var next *TreeNode
			if o {
				next = arr1[i]
			} else {
				next = arr1[len(arr1)-i-1]
			}
			level = append(level, next.Val)
			if arr1[i].Left != nil {
				arr2 = append(arr2, arr1[i].Left)
			}
			if arr1[i].Right != nil {
				arr2 = append(arr2, arr1[i].Right)
			}
		}
		result = append(result, level)
		arr1 = arr2
		arr2 = []*TreeNode{}
		o = !o
	}
	return result
}
