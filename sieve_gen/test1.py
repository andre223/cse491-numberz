import sieve

def test1():    
    s = sieve.next()    
    i = iter(s)    
    assert i.next() == 3 

test1()
