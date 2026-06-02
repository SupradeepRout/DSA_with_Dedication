'''
Problem Link :https://leetcode.com/problems/insert-interval/submissions/1994614272/
Video Link : https://www.youtube.com/watch?v=yAopxaHmRn0&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=35
Level : Easy
'''

class Insert_interval : 
    def insertt(self , intervals:list[list[int]], newInterval:list[int] )->list[list[int]] : # it manage the insertion of the given intervals 
        if not intervals:
            return [newInterval]
        
        n =len(intervals) 
        
        for i in range(n):
            if intervals[i][0] >= newInterval[0] :
                intervals.insert(i,newInterval)
                break
        else:
            intervals.append(newInterval)
            
        return self.mergee(intervals)
    
    def mergee(self , nums:list[list[int]])-> list[list[int]]: # It managee the merging of the intervals
        n = len(nums)
        start1 = nums[0][0]
        end1 = nums[0][1]
        res = []
        
        for i in range(1,n) :
            start2= nums[i][0]
            end2= nums[i][1] 
            
            if end1 >= start2 :
                end1 = max(end1 , end2)
            
            else:
                res.append([start1,end1])
                start1 = start2
                end1 = end2
            
        res.append([start1,end1])
        return res    
    
        
                    
                    
if __name__ =="__main__":
    #array = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    array=[]
    interval = [4,8]
    obj = Insert_interval()
    res = obj.insertt(array ,interval)
    print(res)
    