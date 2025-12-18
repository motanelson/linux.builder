import os
print("\033[40;37m\ncommand line version 0.01v\n")
while(True):
    print(":>",end="")
    i=input().strip()
    if i=="":
        break
    os.system(i)
    
