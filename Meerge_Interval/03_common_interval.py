'''
Definition : Common interval
Link :
'''


class Common_interval:
    def intervalIntersection(self, first: list[list[int]], second: list[list[int]]) -> list[list[int]]:
        m = len(first)
        n = len(second)
        i,j =0,0 
        res= []
        
        while( i<m and j<n):
            start1 = first[i][0]
            end1 = first[i][1]
            start2=second[j][0]
            end2 = second[j][1]
            
            if start1 < start2 :
                if end1 >= start2 :
                    begin = max(start1 , start2)
                    end = min(end1 , end2)
                    res.append([begin,end])
            else :
                if end2 >=start1 :
                    begin = max(start1 , start2)
                    end = min(end1 , end2)
                    res.append([begin,end])
            if end1 <= end2 :
                i+=1
            else :
                j+=1
                
        return res

if __name__=="__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]] 
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    obj=Common_interval()
    ans = obj.intervalIntersection(firstList,secondList)
    print(ans)