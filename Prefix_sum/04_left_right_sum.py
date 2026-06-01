# problem Link :https://leetcode.com/problems/left-and-right-sum-differences/
class difference_left_right_sum:
    def difference(self , nums:list[int])->list[int]:
        prefix_sum = 0
        arr_sum = sum(nums)
        n = len(nums)
        ans =[]
        
        for i in range(n):
            suffix_sum = arr_sum - prefix_sum - nums[i]
            result = abs(prefix_sum - suffix_sum)
            ans.append(result)
            prefix_sum += nums[i]
        return ans
if __name__ =="__main__":
    arr =[10,4,8,3]
    obj = difference_left_right_sum()
    answer = obj.difference(arr)
    print(answer)