list_of_string=['apple','orange','grape','mango']
x=str(input("Enter the string to be searched:"))
found=False
for i in range(len(list_of_string)):
         if(list_of_string[i]==x):
                 found=True
                 print("%sfound at %dth position"%(x,i))
                 break
if(found==False):
       print("%s is not in string"%x)
