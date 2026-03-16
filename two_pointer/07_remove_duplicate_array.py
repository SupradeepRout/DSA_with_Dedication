class remove_duplicate :
    
    def rmv_dup(self ,nums : list[int])->list[int] :
        n = len(nums)
        low , high = 0 , 1
        while(high < n):
            if(nums[low] != nums[high]):
                low += 1
                nums[low] = nums[high]
            high += 1
        return nums[:low+1]
    
if __name__ == "__main__" :
    arr = [1,1,1,2,2,3,4,5,5,5,6,6,7]
    obj = remove_duplicate()
    print(f"The final list after removing duplicates is : {obj.rmv_dup(arr)}")
    