#Define a custom comparison function 
#without using lambda and bin function 

#comparison function[bitwise operation]


#Option 1: Without using built in functions 

class Solution:

    def cnt(arr):
        return bin(arr).count('1')   #converts arr into binary rep and counts 
    
    return sorted(arr, key=lambda x: (cnt(x), x))