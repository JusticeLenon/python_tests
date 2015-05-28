'''
Several useful functoins for doing things with tuples
'''

def tuple_value_change(tup, x):
    newtup = (x,)
    print tup
    print x
    tup = tup[1:]
    newtup = newtup + tup
    return newtup

