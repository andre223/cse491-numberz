import sieve

def test3():    
    s = sieve.next()    
    i = iter(s)    

    for x in range(8):        
	i.next()    
    assert i.next() == 29


test3()
