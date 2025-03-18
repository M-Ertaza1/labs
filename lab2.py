# Python program to illustrate 
# while loop 
count = 0 
while (count < 3): 
 count = count + 1 
 print("Hello Geek") 






# Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
 print(i) 


#Example 2 
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
 print(i) 


#Example 3 
# Iterating over a String 
print("\nString Iteration") 
s = "Geeks" 
for i in s : 
 print(i) 


 # Iterating by index 
list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
  print (list[index])


  # Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
  if letter == 'e' or letter == 's': 
   continue 
print('Current Letter :', letter)



# break the loop as soon it sees 'e' 
# or 's'
for letter in 'geeksforgeeks':  
 if letter == 'e' or letter == 's': 
  break 
print('Current Letter :', letter)


# Creating a Function
def my_function(): 
 print("Hello from a function") 

#Calling a Function 
my_function() 





