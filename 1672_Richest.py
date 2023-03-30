accounts = [[1,2,3],[3,9,1]] 

def maximumWealth(accounts):
    wealth =  0 
    for i in accounts: 
        if sum(i) > wealth:
            wealth = sum(i) 
    return wealth
print(maximumWealth(accounts))