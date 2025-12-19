import os
def copys(s1:str,s2:str):
    s=b""
    try:
        f1=open(s1,"rb")
        f2=open(s2,"wb")
        s=f1.read()
        f2.write(s)
        f1.close()
        f2.close()
    except:
        print("file error: "+s1)
def removessp(s):
    ss=s
    while(True):
        if ss.find("  ")<0:
            break
        ss=ss.replace("  "," ")
    return ss
print("\033[40;37m\ncommand line version 0.01v\n")
while(True):
    print(":>",end="")
    i=input().strip()
    
    if i=="":
        break
    i=removessp(i)
    ii=i.split(" ")
    iii=ii[0].strip().lower()
    t=True
    if iii=="echo" or iii=="printf":
        print(" ".join(ii[1:]))
        t=False
    if iii=="mkdir":
        os.makedirs(ii[1], mode=0o777, exist_ok=False)
        t=False
    if iii=="cd":
        os.chdir(ii[1])
        t=False
    if iii=="cwd":
        print(os.getcwd())
        t=False
    if iii=="ls" or iii=="dir":
        print(" ".join(os.listdir()))
        t=False
    if iii=="set":
        os.putenv(ii[1],ii[2])
        t=False
    if iii=="path":
        print(os.getenv("path"))
        t=False
    if iii=="copy" or iii=="cp":
        copys(ii[1],ii[2])
        t=False
    if iii=="cat" or iii=="type":
       t=False
       iiii=i.split(">")
       aa=iiii[0].strip()
       aa=removessp(aa)
       r=""
       aa=aa.split(" ")
       index=0
       for n in aa:
          if index!=0:
              f1=open(n,"r")
              rr=f1.read()
              r=r+rr
              f1.close()
          index=index+1  
       if len(iiii)>1:
           f1=open(iiii[1].strip(),"w")
           f1.write(r)
           f1.close()
       else:
           print(r)
    if iii=="exit":
       break
    if t:
        os.system(i)
    
