# this is an implementation of the 'series' functionality using
# a generator.

def adder():
    n = 0
    while 1:  # while true
        n += 1 
        yield n # returns generated n
