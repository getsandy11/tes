print("Hello Sandeep")
x=1.0
print (type(x))
print (3 * "Hell"+"pp")
print (id(x))

import keyword
print (keyword.kwlist)
a=(keyword.kwlist)
print (a)

# type conversion in python ( type decided dynamic and we can change in fly)
""" int() 
float()
ord() > return unicode
str()
complex()

Other functions are 
dict()
tuple()
list()
set()

"""
x = 5
print (type(x))

y="22"
print (type(y))

z=x+float(y)

print (z)
x="33"
x=int(x)
print (type(x))

x='a'
y=ord(x)
print(y)


# Handelling number system in python
"""
1. Decimal (0 to 9) (571)10
2. binery (0 and 1) (10011)2
3. Octal (0 to 7) (432)8
4. hexadecimal ( 0 to 9 and ABCDEF) (3fa2)16


x=0b101 (binery) or x=0B101
x=0o42 (octal) x=0O42
x=0x3f (hex)x=0X3f


"""

x=0b101
print(x)
print(type(x))

x=0o10
print(x)

x=0X3f
print(x)
print(hex(x)) # hex function will print hex value
x=0o10
print(oct(x)) # octal
x=0B101
print(bin(x)) # binery
y=bin(x) 
print(y[2::]) # slicing

#operators 
""" operators are special symbol in python that carries the arithmatic and logical computation 
operators requires operand (data) to perform its job

 7 category 

@ Arithmatic : + - * / 
@ Relational : comparison 
@ Logical  : and or not
@ Bitwise : bit
@ Assignment : ==
@ Identity : 
@ Membership : 


++ increment -- decrement operator 
x=4
x++
x= ? x= 5 now
x-- 
x= ? x= 4 now
"""

x=3+4
print (x)
y=x 
print(y)


# Arithmatic operators (7)
"""
** 3**2 Exponent
/ 10/5 Divide (float)
// 5/2 Divide (Floor)
* 5*4 Multiply
% 10%4 Modulas ( also work on floating values)
+ 5+2 Addition
- 5-2 Subtraction 

+ can be used for addition and concatination of string 
* can be used for multiplication and if there is string it can be multiplier x = 3 * ab 
both can not be string / one integer and one string 
"""


x=3**2
print(x)
x=-2**3
print(x)
x=2.5**2
print(x)
x=10**20
print(x)
x=2**128
print(x)

x= 5/2
print(x)
x= 5.0/2.0
print(x)
x=11%7
print(x)
x=2%3 # lower number
print(x)

x=2+3
print(x)
#x=2+"ab" # will give error
x="ab"
y="cd"
z=x+y # 
print(z)
x=3*"ab"
print (x)

# Relational Operator (Comparison operators) (6)
"""
> : 3>2 : Greater Than
< : 10<5 : Less Than
>= : 5>= : Greater Than or equal to
<= :5<=4 : Less Than or equal to
== 10==4 : equal to 
!= 5!=4 : Not equal to 

Relational operators always yield true or false as a resut
When truth value converted to int, it becomes 1 or 0
Relation operators can be used to compare string also
Only == and != can work between complex values 

Every non zero. valie is True and zero value is False
True = 1
False = 0 

Relcational operators works on string as well 

"""
x=True
y=int(x)
print(y)

y=int(False)
print(y)
y=bool(4)
print(y)
y=bool(0)
print(y)
print ("hi")
x=("ABC"=="abc")
print(x)
print("hello")
a=("AB" < "CD")
print(a)

#a=(3+4j > 2+3j) # error it will work with == or != and not < > 
a=(3+4j == 2+3j)
print(a)

x=True+55 # special case 
print(x)

a=5>4>3 # True ( all need to be true if not it will be false)
print(a)
print (int(a))

#string and int comparision  ( Error ) 
# But if you use == or != ( Answer)
# == and != will give always result ( check content and type)


print(3+4j == 3+4j)
print('a'==97)
print (ord('a')==97)
print(5==5.0) # exception True 
print(True==1) # exception
print(False==0) # exception
print(True<5)


#Logiacal operators (3)
"""
and : a>b and a> c ( When both operands are true then true) > Binery op. x and y 
or : a>b or a>c ( When both false then result false) > Binery op x and y
not : not a>b invert thr result > Uniery operator  : not x

@logical operators must be return in lowercase only
@Non zero (1) will be treated as True and, zero will ne treated as False
@ Empty string is always False. Non empty string is true

"""
print ("")
print ("Logical Operators")

print ("")
print ( 3> 4 and 5>3)
print(3!=4 and 10<20)
print(4>3 or 3<2)
print( 5 and 4)
print ( 5 and 4)
print(0 and 4)
print (3 and "ab")
print(3 or 5)
print(0 or 5)
print(0 or False)
print (3 or False)
print(not 4 > 3)
print (not 5)
print(not "sandeep")

#bitwise operators ( Works bits 1 and 0 like 1010 )
"""
& 5&6 
| 5|6
~ ~5
^ 5^6
>> 99>>2
<< 5<<3




"""


#Assignment Operators
""" 
=
+=
"""


  #identity operartor 
"""

is 
is not 

"""
x=5
y=5
print(x==y) 
print(x is y)
y=4
print(x is y)
print(id(x))
print(id(y))
x=5
y=5.0
print(x==y)
print(x is y)

# membership operator 
"""
in 
not in 

"""
x="abc"
print("a" in x)
print("A" in x)

#x=256 ( Its not itterables its only one number )
#print(2 in x)

x=[1,2,3,4]
print(2 in x)

print(type(x))
x=1,2,3,4
print(1 in x)

print(type(x))

#Taking Input from User

"""
input method
filtering data ( string / float / integer)
example program 
input()

saved input as string 
"""

#x=int(input("Enter your favourite number: "))
x=22
print (x)
print(type(x))
x=str(x)
print(type(x))
print(x)
print("22" in x )
print("22" is x )
print(type(x))

#use of import and from 

"""
Module is python file consisting of paython code
module can define functions, classes and variables 




































