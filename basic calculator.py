
     
x=input("enter operands seperated with space:")
y=input("enter the operations :")
num1=int(x[0])
num2=int(x[2])
res=[num1+num2,num1-num2,num1/num2]
for i in range(len(y)):
   print(res[i],end=" ")
