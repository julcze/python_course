#1
y = [(2*x^2+2) for x in range (56,101)]
print(y)
print('-'*20)

#2
def fac(x):
    print('Insert your value here:')
    if x>=0:
        factorial=1
        for i in range(1,x+1):
            factorial=factorial *i
        print('The factorial od inserted value is', factorial)
    else:
        print("error")

fac(int(input(": ")))

print('-'*20)
#3

def findmin(x):
    y=min(x)
    z=x.index(y)
    return y, z

print (findmin([1,2,3,5]))