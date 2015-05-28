'''
Several useful functoins for doing things with tuples
'''
def tuple_value_change (tup, x) :
    newtup = (x,)
    print tup
    print x
    tup = tup[1:]
    newtup = newtup + tup
    return newtup

def tuple_lengths(*tup_len):

    listoflength =[]
    
    #Iterating over each item in tup_len
    for i in tup_len:
        print i
        print len(i)
        listoflength.append(len(i))
    
    return listoflength
