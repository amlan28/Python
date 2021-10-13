#Sample Output:
#Input number of terms: 5
#The even numbers are: 2 4 6 8 10
#The Sum of even Natural Numbers up to 5 terms: 30

num = int(input("Input number of terms: "))  
x=num 
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0    
   print("The even numbers are:")
   for t in range(1,num+1):
       print(2*t)
       sum += 2*t 
   print("The Sum of even Natural Numbers up to",x,"terms:",sum)  
