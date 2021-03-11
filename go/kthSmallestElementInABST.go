package main

import "fmt"

func main() {
	root := &TreeNode{5, nil, nil}
	root.Left = &TreeNode{3, nil, nil}
	root.Right = &TreeNode{6, nil, nil}
	root.Left.Left = &TreeNode{2, nil, nil}
	root.Left.Right = &TreeNode{4, nil, nil}
	root.Left.Left.Left = &TreeNode{1, nil, nil}
	fmt.Printf("Result %d\n", kthSmallest(root, 4))
}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	index := 1
	result := -1
	helper(root, k, &index, &result)
	return result
}

func helper(root *TreeNode, k int, index *int, result *int) {
	if *index > k {
		return
	}
	if root.Left != nil {
		helper(root.Left, k, index, result)
	}

	if *index == k {
		*result = root.Val
	}
	*index += 1
	if root.Right != nil {
		helper(root.Right, k, index, result)
	}
}
