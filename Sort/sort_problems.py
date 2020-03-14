#Given a collection of intervals, merge all overlapping intervals.
#Example 1:

#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:

#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge_intervals(intervals):
        
  intervals = sorted(intervals,key = lambda x:x[1], reverse = False)
  stop = False  
  while stop == False:
    b,j = 1,0
    while j < len(intervals) - 1:
      if intervals[j][1] >= intervals[j+1][0]: #There is overloping
            
        intervals[j][0] = min(intervals[j][0],intervals[j+1][0])
        intervals[j][1] = intervals[j+1][1]
        del intervals[j+1]
        b = 0
            
      else:
        j+=1

    if b == 1:
      break
        
  return intervals

#Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#You may assume that the intervals were initially sorted according to their start times.

#Example 1:

#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]
#Example 2:

#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

def insert(intervals, newInterval):
        
  #Insert the intervals 
  i = 0
  while i != len(intervals):

    if (intervals[i][1] >= newInterval[0] and intervals[i][1] <= newInterval[1]): #Insertion and merging 
      intervals[i] = [min(intervals[i][0],newInterval[0]),newInterval[1]]
      break

    elif (newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]): #Insertion and merging 
      intervals[i] = [min(intervals[i][0],newInterval[0]),intervals[i][1]]
      break

    elif (i == 0) and (newInterval[1] < intervals[0][0]):  #Insert in the beginning
      intervals.insert(0,newInterval)
      return intervals

    elif ( i == len(intervals) - 1 ) and ( intervals[i][1] < newInterval[0] ):  #Insert at the last position
      intervals.append(newInterval)
      return intervals

    elif (intervals[i-1][1] < newInterval[0]) and (intervals[i][0] > newInterval[1]): #Insert without merging
      intervals.insert(i,newInterval)
      return intervals

    else:
      i +=1
        
       
  if len(intervals) == 0: #The input list is empty:
    return [newInterval]

  else:
      
    #Merge the overlapping intervals
    while i != len(intervals) - 1:
      if intervals[i][1] >= intervals[i+1][1]:
        del intervals[i+1]
    
      elif intervals[i][1] >= intervals[i+1][0]:
        intervals[i][1] = intervals[i+1][1]
        del intervals[i+1]
      else: 
        break 

    return intervals     