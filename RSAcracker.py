x = 143

#https://pythonism.wordpress.com/2008/05/17/looking-at-factorisation-in-python/

def primefactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    print factorlist

primefactors(x)