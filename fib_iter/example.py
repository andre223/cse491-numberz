import fib

for n, i in zip(range(5), fib.fib()):  # Gets the returned value of __iter__ 
    print n, i

# additional questions to address:
# - what the heck do 'zip' and 'range' do, and why are they there?
'''	'zip' returns a list of tuples, where the ith tuple contains the 
	ith element for each argument sequences of iterables. 
	'range' is a function that contains iterator progressions. In this 
	example the iterator starts at 0 and ends at 2. '''	
