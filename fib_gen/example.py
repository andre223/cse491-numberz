import fib

for n, i in zip(range(3), fib.fib()):
    print i

print type(fib.fib())
# additional questions to address:
# - what the heck do 'zip' and 'range' do, and why are they there?
