from collections import Counter
# counter is a subclass of dict that helps count hashable objects. 
# It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
# It provides a convenient way to count occurrences of elements in a collection, such as a list or a string.

class min_window_subString : 
    def minwindow(self , s : str , t : str )-> str :
        if s == '' or t == '' :
            return ''
        n= len(s)
        low , high = 0,0 
        dict_t = Counter(t)
        dict_s = {}
        min_len = float('inf')
        start = 0
        
        for high in range(n):
            dict_s[s[high]] = dict_s.get(s[high],0 ) + 1
            while (self.compare(dict_s , dict_t)):
                window_len  = high - low + 1 
                min_len = min(min_len , window_len)
                start = low 
                dict_s[s[low]] -= 1
                low += 1
                
        return s[start : start + min_len] if min_len != float('inf') else ''
        
# this method is used to compare the frequency of characters in dict_s and dict_t to check 
# if dict_s contains all characters of dict_t with at least the same frequency.       
    def compare(self , dict_s , dict_t):
        for key , value in dict_t.items():
            if key not in dict_s or dict_s[key] < value :
                return False
        return True

if __name__ == "__main__" :
    s = input("Enter the string S : ")
    t = input("Enter the string t : ")
    obj = min_window_subString()
    print(f"The minimum window substring is : {obj.minwindow(s,t)}")