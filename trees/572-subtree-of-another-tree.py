class Solution:
    def isSubtree(self, tree: Optional[TreeNode], subtree: Optional[TreeNode]) -> bool:
        if not subtree:
            return True
        if not tree:
            return False
        
        if self.sameTree(tree,subtree):
            return True
        
        return self.isSubtree(tree.left, subtree) or self.isSubtree(tree.right, subtree)


    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right) 
