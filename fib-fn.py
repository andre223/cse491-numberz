last_1 = 1
last_2 = 1

def next():
    global last_1, last_2  #use the global last_1 and last_2

    next_fib = last_1 + last_2   #store the sum of last_1 and last_2 
    last_1, last_2 = last_2, next_fib    #re-assignment of the variables.
                     # last_1 = last_2 && last_2 = next_fib 
    return next_fib

print next()
print next()
print next()
