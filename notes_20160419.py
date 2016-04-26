field = [[0 for i in range(32)] for j in range(39)]
field [2][3]



f = open("file.txt", "wt")
f.write("string")
f.flush()
# or use "less"
less file.txt
#if we use "close" we will lost all info
f.close()


#openinf file for reading NEVER TO USE!!!!!!!!!!!!!!!!!!!!!!!!!!!
f = open("file.txt", "rt")
#Now we will read our file

#first method, WILL output info from file
s = f.read()
#cursor now in the end of our file, so if we make input again ir will be...

#second method
f = open("file.txt", "rt")
s = f.read(8)
#>>> s
#"String
#>>> f.tell()    - it show us where our cursor(ukazatel) is
#>>> 8

#Method 3 for text file we could read string by string
f = open("file.txt", "rt")
f.readline()

#for example
while True:
    s = f.readline()
    if not s:
        break
    print(s)

#Method 4. we could use"for", it save in RAM (if I understand right

f = open("file,txt", "rt")
for line in f:
    print(line)
f.close()

## For search and writing
f.write("String\n")
f.seek(+/-n,0/1/2)       # to set position in file
# 0 - position for

f.seek()



## we need to close files   ALWAYS USE IT!!!!!!!!!!!!!!!!!!!!!!!

with open("file.txt", "r") as f:
    s = f.read()
    for i in f:
        print(i)
#>>> f.closed == True


## function that return physical number of our file
f.fileno()
#>>> 4


# Python have built-in serialization

import pickle    # or _pickle

obj = [1, 2 [2, 4, 2.4], "aaa", [True, False]]
s = pickle.dumps(obj)
obj1 = pickle.loads(s)    #(s) mean string
obj = obj1


## >>> pickle.dump(obj, open("obj.pickle", "wb"))
## >>> pickle.load(open("obj.pickle", "rb"))
