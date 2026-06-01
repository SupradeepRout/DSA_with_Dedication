# Problem Link : https://leetcode.com/problems/range-sum-query-immutable/submissions/1993315289/
class range_sum :
    def __init__(self , nums):
        self.pre_sum =[0]
        for i in nums:
            self.pre_sum.append(self.pre_sum[-1] + i )
    
    def sumRange(self , left , right):
        return self.pre_sum[right + 1] - self.pre_sum[left]
    
if __name__ =="__main__":
    arrayy = [-2,0,3,-5,2,-1]
    obj = range_sum(arrayy)
    print(obj.sumRange(0,2))
    print(obj.sumRange(2,5))
    print(obj.sumRange(0,5))