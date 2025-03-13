#print hallo world
print ("hallo world....")


#single line comment
x=1
#initiallize x with 1
if x>0:
     print("these are two comments")


#input/output
txt=input("Type something to test this out:")
print(txt) 

#multiple statements in a single line
print("statement");print("statement2")

#indentions
x=1
if x>0:
 print("single space indention") 

x=2
if x>1:
    print("single space+tab indention") 


#data types
#integer
a=1235
print(type(a))


b=-1235
print(type(b))

c=0
print(type(c))


#data types
#float
a=12.35
print(type(a))


b=-123.5
print(type(b))

c=.35
print(type(c))

d=2.12e-10
print(type(d))

e=5e220
print(type(e))



#complex
a=complex(1,2)
print(type(a))
print(a)


b=1+2j
print(type(b))


#boolean
a=True
print(type(a))
print(a)


b=False
print(type(b))

#string

str1="strings1"
print(str1)

str2='strings2'
print(str2)

#escape sequence
print("this  is a backslash \\ mark")

print("this  is a tab \t mark")

print("this  is a new \n line")

print("these are \'single quote \'")

print("these are \"double quote \"")


#accessing string elements
string1="python tutorial"
print(string1[0]) #print first character
print(string1[-15]) #print first character
print(string1[14]) #print last character
print(string1[-1]) #print last character
print(string1[4]) #print 4th character
print(string1[-11]) #print 4th character
#print(string1[16]) #out of index range



#LISTS
my_list=[5,10,15,20,25]
print(my_list)

my_list2=['red','blue','white']
print(my_list2)

my_list3=['red',20,20.20]
print(my_list3)

color=['red','white','grey','blue','black']
print(color[0])
print(color[1],color[2])
print(color[-1])