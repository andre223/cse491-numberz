n = 0  # 1. n is set to 0.

def add_one():
    global n
    n = n + 1
    return n

print add_one()
print add_one()
print add_one()
