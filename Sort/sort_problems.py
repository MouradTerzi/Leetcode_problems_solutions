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
