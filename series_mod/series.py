# this is an implementation of the 'series' functionality using a module.

n = 0 # Sets n to 0

def add_one():
    global n  # Sets a global n, init value 0. 
    n = n + 1 # increment n by 1
    return n

# additional questions to address:
#  - what does 'global' do, above?
#	Uses the n thats defined locally and uses it as a global variable.

#  - what naming limitations are there on series.py? Could we name it
#        series_mod.py or series-mod.py, and still have it work as a module?

#	As long as the correct
