# use  declaring a function
Example 1:
def int():
    print("HI, I'm ameer mavia khah")
    print("My Father Name Is Aamir Khan")
    print("I'm Student for Bano Qabil 20.")
int()

Example 2:
# python program to demonstrat
#default argements
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
    #Driver Code
myFun(10)

Example 3:
# Python Parameterized Function
def evenodd(x):
    if (x%2==0):
        print("even")
    else:
        print("odd")
evenodd (2)
evenodd (3)

Example 4:
# Python keyword argument

def student(firstname, lastname):
    print(firstname, lastname)
#keyword arguments
student (firstname ='Geek', lastname='practice')
student (lastname ='Practice', firstname='Geek')

Example 5:
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("sum: ",sum)
#function call with two values
add_numbers(5,4)
