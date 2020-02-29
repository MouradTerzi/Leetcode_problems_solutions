import os 
import sys 


#Recursive Branch and bound wihtout recursive variable

def recursive_branch_and_bound(rem_weight,ind,w_t,p_t,p_s,c_p_s,b_s,c_b_s):

  if ind == len(w_t) - 1: #The last element in the weight table 
    for i in range(int(rem_weight/w_t[ind])+1):
      if (c_p_s + i*p_t[ind]) > c_b_s:
        c_b_s = c_p_s + i*p_t[ind] #Update the best solution cost 
        b_s = p_s[:]  #Update the current best solution 
        b_s.append(i) #Update current best solution 

  else: #The current element is not the last element in the list 
    for i in range(int(rem_weight/w_t[ind])+1):
      e = c_p_s + i*p_t[ind] + ((rem_weight - i*w_t[ind])/w_t[ind+1])*p_t[ind + 1]  #Evaluation of the new child node
      if e > c_p_s:  #Depth exploration of the new child node
        p1_s = p_s[:] #Use another variable in order to not lose the current partial solution 
        p1_s.append(i) 
        b_s, c_b_s = recursive_branch_and_bound(rem_weight - i*w_t[ind], ind+1, w_t, p_t, p1_s, c_p_s + i*p_t[ind], b_s, c_b_s)

  return b_s, c_b_s
           

#A simple test of the function 
rem_weight = 130
ind = 0
w_t = [33,49,60,32]
p_t = [4, 5, 6, 2]
p_s = []
c_p_s = 0
b_s = [3,0,0,0]
c_b_s = 12

b_s, c_b_s = recursive_branch_and_bound(rem_weight,ind,w_t,p_t,p_s,c_p_s,b_s,c_b_s)

print(b_s,c_b_s)

          
      