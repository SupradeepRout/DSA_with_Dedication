'''given an array that contain different colour of baloon ,
and I have to return the 1st colour of the baloon which presnt in odd numbere 
'''
from collections import Counter
class colour :
    def count(self , arr):
        cnt =Counter(arr)
        
        for i in cnt:
            if cnt[i] % 2 != 0 :
                return i 
        return "e"
        
if __name__ =="__main__":
    n= int(input("enter the size of the array : "))
    baloon = [input() for _ in range(n)]
    obj = colour()
    clr = obj.count(baloon)
    print("all are even") if clr =="e" else print(f"the odd colour is :{clr}")