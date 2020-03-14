import numpy as np 

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

#[1,2,3,4,5]
#2
#Output
#[1,2,3,5]
def removeNthFromEnd(head, n):
        
  List_node=list()
  List_node.append(head)
  current=head
  while current.next!=None:
    List_node.append(current.next)
    current=current.next
      
  ind=len(List_node)-n
  if ind ==0: #Remove the head
    head=head.next
  else: #Remove another element different than the head
    prev=List_node[ind-1]
    prev.next=List_node[ind].next
          
  return head

#Input: 1->2->3->4->5->NULL, m = 2, n = 4
#Output: 1->4->3->2->5->NULL
def reverseBetween(head, m, n):
  
  if head!=None and head.next!=None:  #The input list has more than two elements
    i=1
    current=head  
    old_prev=head
    while i<m and current!=None:
      old_prev=current
      current=current.next
      i+=1
    
    saved_node=current
    prev=current
    current=current.next
    while i<n and current!=None:
      new=ListNode(current.val)
      new.next=prev
      prev=new
      current=current.next
      i+=1
    
    if m!=1:
      old_prev.next=prev
      saved_node.next=current
    else:
      old_prev.next=current
      return prev
          
  return head 


#Algorithm of Insertion Sort:
#Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
#At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
#It repeats until no input elements remain.

#Example 1:
#Input: 4->2->1->3
#Output: 1->2->3->4

#Example 2:
#Input: -1->5->3->4->0
#Output: -1->0->3->4->5

def insertionSortList(head):
        
if head != None: #The input list is not empty 
  new_head = ListNode(head.val)
  head = head.next 
  while head != None:
    
    current = new_head 
    while current.val < head.val:
      if current.next != None:
        if current.next.val > head.val: 
            break
        else:
            current = current.next #Explore the rest of the list to find the best position 
      else: #The current is the last element of the new list 
        break 
    
    #Insertion of the element in the new list
    new_node = ListNode(head.val)
    
    if (current == new_head) and (current.val < head.val): #Example  current.val == -1 and head.val == 5            
      new_node.next = new_head
      new_head = new_node
      
    else:
      new_node.next = current.next
      current.next = new_node
    
    head = head.next
    
  return new_head