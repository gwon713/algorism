def fibonacci_Recurcive(num):
    return fibonacci(num-1) + fibonacci(num-2)
        
def fibonacci(num): 
    if 0 <= num <= 1 :
        return num
    else :
        return fibonacci_list(num)        

print(fibonacci(10))