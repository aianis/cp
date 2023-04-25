class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        #1. Create a dictionary to record number of multuple occurences 
        count = {}

        #itreate over the arr and check the occurences 
        for num in arr:
            count[num] = count.get(num, 0) + 1 
        return len(count) == len(set(count.values()))
        

        