num = 8 
def step_reduce_zero(num):
    counter = 0 
    for i in num:
        if i%2 == 0:
            counter += 1
    return counter 
print(step_reduce_zero(num))