#Sample Output:
#Input 1st number for LCM: 15 
#Input 2nd number for LCM: 25
#The LCM of 15 and 25 is: 75


def hcf(x, y):
   
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i
     
   return hcf 
  
num1 = int(input("Input 1st number for LCM: "))  
num2 = int(input("Input 2nd number for LCM: ")) 
lcm=int((num1*num2)/hcf(num1, num2))
print("The L.C.M. of", num1,"and", num2,"is",lcm)
