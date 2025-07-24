a = int(input("Enter your age:"))

if(a>=18):
     print("you are eligible to vote")
     print("congratulations")
     
elif(a<0):
    print("you are entering an invalid negative age")
    
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
     print("you are mot eligible to vote")
     
print("end of program")


