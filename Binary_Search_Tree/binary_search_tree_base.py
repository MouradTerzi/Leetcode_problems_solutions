import os 
import numpy as np 
import pandas as pd 

#Iterative methods
#Method 1: Search of a giving element   
#Method 2: Insertion of an element in the BRT
#Method 3: Creation of a Tree from a list of elements 
#Method 4: Delete an element  
#Method 5: Iterative Inorder exploration of a given BRT
#Method 6: Iterative Preorder exploration of a given BRT

#Definition of the TreeNode structure 
class TreeNode: 
    def __init__(self,data,prec):
      self.prec = prec
      self.data = data
      self.left_node = None
      self.right_node = None

########################################################################################################
########################################################################################################
######################################## Creation of an BRT ############################################
########################################################################################################
########################################################################################################

def SearchInBRT(root,target):
  if root == None:
    print("Empty tree !!")
    return -1
  else:
    current = root
    prec = None
    while current!=None:
      if current.data == target:
        #print("The element ", target, "is in the input tree")
        return True,prec,current
      else:
        prec = current
        if current.data < target:
          current = current.right_node
        else:
          current = current.left_node
    
    return False, prec, None 


########################################################################################################

def InsertionInBRT(root, target):
  
  if root == None:
      root = TreeNode(target, None)
  else:
    boolean,prec,_ = SearchInBRT(root,target)
    if boolean == False:     #The element is not in the tree
      new_leaf = TreeNode(target,prec) #Creation of the new leaf which contain the element e
      if prec.data > target:              
        prec.left_node = new_leaf     
      else:
        prec.right_node = new_leaf
    else:
      print("The element ",target," is already in the input tree")
  return root 


########################################################################################################

def CreateBRT(elements_list):
  
  if len(elements_list) == 0:
    print("There is no elements to insert in the new tree")
    return -1
  else:
    root = None
    for e in elements_list:
      root = InsertionInBRT(root,e)
    return root
 
  return root

########################################################################################################

def DeleteElementFromBRT(root,target):
  if root == None:
    print("Can't delete from an empty tree !!!")

  else:
    boolean, prec, element = SearchInBRT(root,target)
    if boolean == False:
      print("The element is not in the input tree")

    else: 

      if element.left_node == None and element.right_node == None: #The element is a leaf
        if prec != None:  #The element is not a root 
          if prec.left_node == element:
            prec.left_node = None
          else:
            prec.right_node = None 
        
        else:  #The element to delete is the root of the tree and it has no left_node and a right_node
          return None 
    
      elif element.left_node == None:   #The element has a right_node as child
        if prec != None: #The element to delete is not the root of the tree
          if prec.left_node == element:
            prec.left_node = element.right_node
          else:
            prec.right_node = element.right_node
        
        else: #The element to delete is the root and it has only a right_node
          return element.right_node

      elif element.right_node == None:  #The element to delete has a left_node 
        if prec != None: #The element to delete is not the root of the tree
          if prec.left_node == element:
            prec.left_node = element.left_node
          else:
            prec.right_node = element.left_node
        else: #The element to delete is the root and it has only the left node 
          return element.left_node

      else:  #The element to delete has a left_node and right_node
          min_right_node = element.right_node
          prec_min_right_node = element

          while min_right_node.left_node != None:  #Get the node with minimum value from the right of element
            prec_min_right_node = min_right_node
            min_right_node = min_right_node.left_node
          
          element.data = min_right_node.data   #Replace the value of element by the value of min_right_node
          if prec_min_right_node != element:   #In this case, the right node of element has its left_node
            prec_min_right_node.left_node = None
          else: #In this case, the right node of element is not a tree
            element.right_node = None
  
    return root 

########################################################################################################
########################################################################################################
######################################## Exploration of an BRT #########################################
########################################################################################################
########################################################################################################

def IterativeInorder(root):

  stack = list() #Declaration of the stack in order to save the nodes between the tree courses
  current = root 

  if current == None:
    print("The tree is empty !!")
  else:
    
    print("Iterative inorder of the input tree !!")
    if current.left_node == None and current.right_node == None:
      print(current.data) #Show the value of the root 
      return 

    else:
      
      while current != None and current.left_node == None:
        print(current.data)
        current = current.right_node
      
      if current != None:  #Exploration of the tree 
        stack.append(current)
        current = current.left_node
        while len(stack) != 0:
          stack.append(current)  #Add the current node to the stack
          if current.left_node !=None:
            current=current.left_node
          else:
            while len(stack) != 0:
              current = stack.pop()
              if current != None:
                print(current.data)
                if current.right_node != None:
                  current = current.right_node
                  stack.append(None)
                  break 

      return   

########################################################################################################

def IterativePreorder(root):
  
  if root == None:
    print("The tree is empty !!!")
    return 
  
  else:
    stack = list() #Declaration of a stack to save the nodes during the tree exploration
    current = root 
  
    if current.left_node == None and current.right_node == None:
      return 
    
    while current != None and current.left_node == None:
      print(current.data)
      current = current.right_node
    
    if current != None:

      print(current.data)
      stack.append(current)
      current = current.left_node

      while len(stack) != 0:
        print(current.data)
        stack.append(current) #Add the current element to the stack
        if current.left_node != None:   #Exploration of the sub left tree of the current node
          current = current.left_node
        else:
          while len(stack) != 0:
            current = stack.pop()
            if current != None and current.right_node != None:
              current = current.right_node
              stack.append(None)
              break 
      
    return 

########################################################################################################

def IterativePostorder(root):

  if root == None:
    print("The tree is empty !!!")
    return 
  
  else:
    stack = list()
    InterNodes = list()
    current = root 
    while current != None and current.left_node == None: #In the case in which current node doesn't have a left node child
    
      InterNodes.append(current)
      current = current.right_node
    
    if current != None:  
      stack.append(current) #Suppose that the root has a left node as child
      if current.right_node != None:
        InterNodes.append(current) #Suppose that the root has a right node as child

      current = current.left_node
      while len(stack) !=0 or len(InterNodes) !=0:
       
        stack.append(current) #Add the current node to the stack 
        if current.right_node != None: #Add the current node to the InterNodes list
          InterNodes.append(current)
        
        if current.left_node != None: #Move to the next node in the left branch of the current node
          current = current.left_node
          #print("current node:",current.data)
        else: #Pop the nodes from the stack and InterNodes and show theirs corresponding values 
          
          while len(stack) !=0:
            current = stack.pop()    
            if current.right_node != None: #Add the node to Internodes list and report the show of its values 
              current = current.right_node
              break

            else: 
              print(current.data)
              while current.prec in InterNodes and current == current.prec.right_node and current.prec not in stack:
                current = InterNodes.pop()
                print(current.data)

    else: #In this case the input tree is a list in which the root value is the smallest value     
      print("The input tree is a list in which the root is the smallest value")     
      while len(InterNodes) !=0:
        print(InterNodes.pop().data)
    
    return 

########################################################################################################

def IterativeBreadthFirst(root):
  
  if root == None:
    print("The input tree is empty !!!")
  else:
    queue = list()
    queue.append(root)
    while len(queue) != 0:
      current = queue[0]
      del queue[0]
      print(current.data)
      if current.left_node != None:
        queue.append(current.left_node)
      
      if current.right_node != None:
        queue.append(current.right_node)
        
    return 0
  
      
      
        







        
        
      

