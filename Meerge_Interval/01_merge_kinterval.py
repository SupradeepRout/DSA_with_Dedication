'''
Problem Link : https://leetcode.com/problems/merge-intervals/description/
Video Link : https://youtu.be/aH5aeejuJU8?si=I-xJEVNXlgMshyah
'''
class Merge_interval: 
    def mergee(self , nums:list[list[int]])-> list[list[int]]:
        if not nums:
            return []
        
        nums.sort()
        
        n = len(nums)
        start1 = nums[0][0]
        end1 = nums[0][1]
        res = []
        
        for i in range(1,n):
            start2 = nums[i][0]
            end2 = nums[i][1]
            
            if(end1 >= start2):
                start1 = start1
                end1 = max(end1 ,end2)
                continue
            
            res.append([start1,end1])
            start1=start2
            end1 = end2
            
        res.append([start1 ,end1])
        return res
        