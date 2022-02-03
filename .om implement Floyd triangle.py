print("Enter'x'to exit")
ran=input("upto how many lines?")
if ran=='x':
     exit()
else:
      rang=int(ran)
      k=1
      for i in range(1,rang+1):
            for j in range(1,i+1):
                    print(k,end="")
                    k=k+1
            print()
    
