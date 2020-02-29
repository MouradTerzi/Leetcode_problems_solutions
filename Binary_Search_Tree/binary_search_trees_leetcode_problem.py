# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

#Methods 
#1 Binary Search Tree to Greater Sum Tree


def bstToGst(self, root: TreeNode) -> TreeNode:
  if root != None:
    stack = list()
    stack.append(None)
    current = root
    cpt = 0
    while len(stack) != 0:
      stack.append(current)
      if current.right != None:
        current = current.right
      else:
        while len(stack) != 0:     
          current = stack.pop()
          if current != None:
            current.val = current.val + cpt
            cpt = current.val
            if current.left != None:
              current = current.left
              break
            
            
  return root         
        