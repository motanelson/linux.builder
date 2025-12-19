import os
import time
from datetime import datetime
def editline(i):
    r=""
    if os.path.exists(i):
        f1=open(i,"r")
        r=f1.read()
        f1.close()
        print(r)
    while(True):
        ii=input()
        iii=ii.strip()
        if iii=="":
            break
        f1=open(i,"a")
        f1.write(ii+"\r\n")
        f1.close()
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
    if iii=="editline" or iii=="edit" or iii=="edlin":
        t=False
        if len(ii)>1:
            editline(ii[1])
    if iii=="hex" or iii=="hexedit":
       t=False
       if len(ii)>1:
           f1=open(ii[1],"r")
           r=f1.read()
           f1.close()
           r=r.encode("utf-8")
           r=str(r)
           r=r[1:]
           
           r=r.replace("'"," ")
           print(str(r))
    if iii=="label":
        t=False
        r="\n".join(os.listdrives())
        print(r)
    if iii=="cls" or iii=="clear":
        t=False
        print("\033c")
    if iii=="color":
        t=False
        if len(ii)>1:
            if(len(ii[1])>1):
                r=ii[1]
                print("\033[4$1;3$2m".replace("$1",r[0:1]).replace("$2",r[1:2]))
    if iii=="print":
        t=False

        if len(ii)>1:
        
            f1=open(ii[1],"r")
            r=f1.read()
            f1.close()
            f1=open("lpt","w")
            f1.write(r)
            f1.close()
    if iii=="sleep":
        t=False

        if len(ii)>1:
            time.sleep(int(ii[1].strip()))
    if iii=="time" or iii=="date":
        today = datetime.today()
        formatted_date = today.strftime("%d-%b-%y")
        t=False
        print(formatted_date)
    if t:
        os.system(i)
    
