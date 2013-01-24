import sieve

def test2():
    s = sieve.next()
    i = iter(s)

    for x in range(4):
	i.next()

    assert i.next() == 13

test2()
