#Function fabric
def f(n):
    def g(x):
        return n * x
    return g
double = f(2)
triple = f(3)


l = []


# Not closed, because depends on i value
for i in range(10):
    def f(x):
        return x * i
    l.append(f)

#closed
for i in range(10):
    def f(x, i=i):
        return x * i
    l.append(f)


# map func operate function to whole container
def double(x):
    return 2 * x
l = list(map(double, [1, 2, 3, 4, 5]))
print(l)


#
def double(x):
    print("double: {}".format(x))
    return x * 2
for i in map(double, [1, 2, 3, 4, 5]):
    print(i)
    if i >5:
        break

#Выводим нечетные числа
def odd(x):
    return x % 2

l = list(filter(odd, [1, 2, 3, 4, 5]))
print(l)

## READ itertools !!!!!!!!!!!!!!!!!!!!!!


#lambda - using for temporary function
list(map(lambda x: 3 * x, [1, 2, 3, 4, 5]))



# поставить неограниченое количество аргументов
def f(*args):
    print(args)

def sum_(*args):  # could set sum(a, *args) to show that we need at least one parameter
    s = 0
    for i in args:
        s += i
        return s
    
def f(*args, **kwargs):
    print(args, kwargs)
    
#>>>f (1,2,3, a=4, b=5)
#(1, 2, 3) {'a' : 4, 'b' : 5}

def f (a, b, c):
    return a + b + c
t = 1, 2, 3
f(*t)

# Обертка!!!!!!!!!!!!!!!!!!!!!!!!! Wrapper
def g (*args, **kwargs):
    print('g')
    return f(*args, **kwargs)


                            #DECORATORS
def decor(f):
    def wrapper():
        print("in")
        res = 
        
#special syntax for decorators
@scale                 # the same as  scale = scale(double)
def double(x):
    return 2 * x

#multiple variants

actions = {1: a, 2: b, 3: c}
def default():
    print('default')
actions.get(5, default)()
actions.get(3, default)()
