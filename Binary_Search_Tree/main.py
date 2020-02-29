from binary_search_tree_base import *

elements_list=[10,15,18]
#elements_list = [8,7,10]
#elements_list = [90,10]
#elements_list=[8]
root = CreateBRT(elements_list)
#IterativePostorder(root)
IterativeBreadthFirst(root)
#IterativeInorder(root)
#root = InsertionInBRT(None,5)
#print(id(root))
#print(root.data)
#print(root.prec)
#print(root.left_node)
#print(root.right_node)
#InsertionInBRT(root,12)
#print(root.right_node.data)
#right = root.right_node
#print(id(right.prec))

#IterativePreorder(root)
#IterativeInorder(root)
#InordreRecursive(root)
#Insertion(root,3)
#Insertion(root,7)
#Insertion(root,10)
#InordreRecursive(root)
#print("Inordre after deleting")
#root = DeleteElement(root,8)
#print("Inordre after deleting:")
#InordreRecursive(root)
#DeleteElement(root,3)
#print("Inordre after second deleting:")
#InordreRecursive(root)
#root = DeleteElement(root,13)
#print("Tree after deleting the node ")
#InordreRecursive(root)
#root=TreeNode(8)
#root.left_node = TreeNode(6)
#root.right_node = TreeNode(11)

#InordreRecursive(root)
#boolean, prec,element = SearchInABM(root,8)
#print(boolean,prec,element.data)
#if boolean == True:
#  print(element.data)
#Insertion(root,8)
#Insertion(root,80)
#Insertion(root,-1)
#print("The tree after insertion of the new elements")
#InordreRecursive(root)
#boolean,prec,element=SearchInABM(root,-1)
#print(prec.data)