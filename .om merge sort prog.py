def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
     if a[0]<b[0]:
        c.append(a[0])
        a.remove(a[0])
     else:
         c.append(b[0])
         b.remove(b[0])
    if len(a)==0:
        c=c+b
    else:
        c=c+a
    return c
def divide(x):
  if len(x)==0 or len(x)==1:
      return x
  else:
      middle=len(x)//2
      a=divide(x[:middle])
      b=divide(x[middle:
                 ])
      return merge(a,b)
x=[39,56,78,96,3,20,1]
c=divide(x)
print(c)
    
