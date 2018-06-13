a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def div(a):                # Define a procedure
    x = []                 # Empty list
    for i in a:            # for i in list a
        if i % 2 == 0:     # i % 2 == 0 then appen append empty list
            x.append(i)
    print (x)              # print x
            
print (div(a))

# CODED BY - GAURAV PADAWE