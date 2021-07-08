def redundant(N):
    stack=[]
    operator=["+","-","%","*","(",")"]
    for i in range (len(N)):
        if (N[i]in operator):
            stack.append (N[i])
        elif (N[i]==')') :
            
          if stack.pop == '(' :
            return 1
        
          stack.pop()
    return 0


N="((a+b))"
a=redundant(N)
if (a==1):
    print("redu")
else:
    print("unredu")
    
        
        
