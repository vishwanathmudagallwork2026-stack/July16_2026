#typecasting ---> means converting the one data type into another data type. In python, we can convert one data type to another data type using built-in functions like int(), float(), str(), etc.

#there are two types of typecasting in python
#1)--> Explicit Type casting
#2)--> Implicit Type casting

#1)---> Explicit type casting
#---> conversion of one data type to another type through manually or done via developer or programmer.add()
#ex.--> str to int
a = "1"
b = "2"
num1 = int(a)
num2 = int(b)
num = num1 + num2
print(num) #Output: integer

#int to float
a = 1
b = 2
num1 = float(a)
num2 = float(b)
num = num1 + num2
print(num) #Output : float



#float to int
x = 3.3
y = 3.45
num1 = int(x)
num2 = int(y)
print(num1 + num2) #Output: decimal will be neglected, so the (3.3 + 3.45) gives the integer only

#these are the some examples of Explicit typecasting

#2)---> Implicit Typecasting
#---> It happens when python automatically converts the one type to another data type through interpreter
#ex-->
a = 2
b = 3
print(a + b) #python automatically converts the data.


