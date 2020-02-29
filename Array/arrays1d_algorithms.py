import os 
import sys 
import numpy as np 
import pandas as pd


#Search_in_rotated_sorted_array
#numMatchingSubseq
#All_permutation
#nextPermutation
#removeDuplicatesFromSortedArray
#twoSum
#Combination sum using a Queue structure 

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
###################################################### Algorithms ##############################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

#Alg 1: Search in a rotated sorted array
#The algorithm is based on the recursivity
#The algorithm's complexity: O(log(N))

def Search_in_rotated_sorted_array(table,target):

  if len(table)==1:
    if table[0]==target:
      return 0
    else:
      return -1
      
  if len(table)==0:
    return -1
  
  else:
    middle=int(len(table)/2)
    if table[middle]==target:
      return middle
    
    else:
      a=self.search(table[0:middle],target)
      b=self.search(table[middle:len(table)],target)
      if (a==-1) and (b==-1):
        return -1
      elif a!=-1:
        return a
      else:
        return b+middle


#Alg 2: The number-of-matching-subsequences in a string S
#Alg 2 is an iterative algorithm
#Example: Inputs:
#               S="abcde"
#               words=["a","bb","acd","ace"]
#         Output: 3

def numMatchingSubseq(S, words):

  numSubseq=0
  list_visited=list()
  for word in words:
    if word not in list_visited:
      min_w,max_w=0,len(word)-1
      min_s,max_s=0,len(S)-1
      while (min_s <= max_s) and (min_w <= max_w):
      
        if S[min_s]==word[min_w]:
          min_w+=1
      
        if S[max_s]==word[max_w]:
          max_w-=1
      
        min_s+=1
        max_s-=1  
          
      if min_w>max_w:
        numSubseq+=1
      else:
        list_visited.append(word)
        
  return numSubseq

#Get all the permutation of a given input array
#Example: input=[1,2,3]
#Output: 1,2,3  1,3,2  2,1,3  2,3,1  3,1,2  3,2,1 

def All_permutation(Array):
  
  if len(Array)==2:
    if Array[0]==Array[1]:
      return [Array]
    else:
      return [Array,[Array[1],Array[0]]]
      
  else:
    List_all_permutation=list()
    Array.sort()
    i=0
    while i < len(Array):
      Array1=Array[:]
      del Array1[i]
      L=All_permutation(Array1)
      for l in L:
        l.insert(0,Array[i])
        List_all_permutation.append(l)
    
      while i < len(Array)-1:
        if Array[i]==Array[i+1]:
          i+=1
        else:
          break
      i+=1      

  return List_all_permutation

#Next permutation of a given input sequence of integers 
#Example: input: 1,2,3 
#         Output: 1,3,2

def nextPermutation(A):
  i=len(A)-1
  while i>0:
    if A[i]<=A[i-1]:
      i=i-1
    else:
      i_min=i
      for j in range(i,len(A)):
        if A[j]>A[i-1] and A[j]<A[i_min]:
          i_min=j
      
      A[i-1],A[i_min]=A[i_min],A[i-1]
      
      for j in range(i,len(A)): #Sort of A
        i_min=j
        for k in range(j+1,len(A)):
          if A[k] < A[i_min]:
            i_min=k
          
        A[j],A[i_min]=A[i_min],A[j]
        
      return A
  
  return A.sort()

#Remove duplicates elements of an input array 
#Example: Input=[0,0,1,1,1,2,2,3,3,4]
#         Output: 0,1,2,3,4

def removeDuplicatesFromSortedArray(A):
  i=0
  while i < len(A)-1:
    if A[i]==A[i+1]:
      del A[i+1]
    else:
      i+=1

  return A, len(A)


#Two sum
#ven nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9
#return [0,1]
def twoSum(Array, target):
        
  i=0
  L=list()
  for i in range(len(Array)):
    L.append([Array[i],i])
  L=sorted(L,key=lambda x:x[0],reverse=False)
  #print(len(L),L)
  i=0
  while i<len(L):
    j=i+1
    while j<len(L):
        print("L[",i,j,"]",L[i][0]+L[j][0])
        if (L[i][0]+L[j][0])==target:
          return [L[i][1],L[j][1]]

        elif (L[i][0]+L[j][0])<target:
          j+=1

        else: 
          j=len(L)
    i+=1
  
  return [-1,-1]
 
#Combination sum using queueu structure
#Input: candidates = [2,3,6,7], target = 7,
#A solution set is:
#[
#  [7],[2,2,3]
#]
def combinationSum(candidates, target):
    
  List_comb = list()
  Queue = list()

  for i in range(int(target/candidates[0])+1):
    if i*candidates[0] <= target:
      c_s = list()
      for j in range(i):
        c_s.append(candidates[0])

      if i*candidates[0] == target:
        List_comb.append(c_s)
      elif len(Queue)>1:
        Queue.append([i*candidates[0],c_s,1])
    
  #Breadth search 
  while len(Queue) > 0:
    c_v,c_s,c_ind = Queue[0][0],Queue[0][1],Queue[0][2]
  
    del Queue[0]
    for i in range(int(target/candidates[c_ind])+1):  #ind == 1, 
  
      if (c_v + i*candidates[c_ind]) <= target:
        c1_s = c_s[:]
        for j in range(i):
          c1_s.append(candidates[c_ind])
          
        if (c_v + i*candidates[c_ind]) == target:
          List_comb.append(c1_s)

        elif c_ind < len(candidates)-1:
          Queue.append([c_v+i*candidates[c_ind],c1_s,c_ind+1])

  return List_comb 