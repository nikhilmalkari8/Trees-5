def recover_tree(root):
    first, second, prev = None, None, TreeNode(float('-inf'))

    # Inorder traversal function
    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return

        inorder(node.left)

        if not first and prev.val > node.val:
            first = prev
        if first and prev.val > node.val:
            second = node
        
        prev = node 
        
        inorder(node.right)

    inorder(root)
    
    if first and second:
        first.val, second.val = second.val, first.val
