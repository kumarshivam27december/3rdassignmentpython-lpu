a="hello,world"
print(a[2:5])
print(a[-5:-1])

print(len(a))
print("word" in a)
print("world" in a)

# casting that is to specify the data type of a variable using casting
x=str(10)
y=int(10)
z=float(10)
print(x,y,z)

# VARIABLES 
# variable name must start with _ or a letter 
# variable cannot start with a number 
# variable name can only contain alphabet,numeric and underscores (_)
# variables name are case sensitive i.e (name,Name,NAME)

# acceptable variables names 
myname='shivam'

# CAMELCASE
myfirstname='shivam'
# PASCALCASE
MyFirstName='shivam'
# SNAKECASE
my_first_name='shivam'

f='my'
g='name'
h='is'

print(f,g,h)
print(f+g+h)  #combined to a single string
print(f+''+g+''+h)


# GLOBAL VARIABLE
# variables that are created outside of a function
# they can be used outside of the function

b='shivam'
def myfunc():
    print("my name is "+ b)
myfunc()    


i='shivam'
def myfunc():
    i='kumar'
    print("my name is" + i)
    myfunc()
    print(x)
    


