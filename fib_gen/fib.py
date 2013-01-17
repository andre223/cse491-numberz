# this is an implementation of the 'fib' functionality using
# a generator.

def fib():
    last_1 = 1 # stored locally in this function
    last_2 = 1

    while 1:
       # next_fib = last_1 + last_2

       # yield next_fib
       yield (last_1 + last_2)
       # last_1, last_2 = last_2, next_fib
       last_1, last_2 = last_2, (last_1+last_2)

# additional questions to address:
# - could you swap the last two lines of the while statement?  what are the
#    plusses and minuses of doing so?
	

# - is there a way to condense the 'while' loop into two statements? try
#    getting rid of the next_fib variable.
