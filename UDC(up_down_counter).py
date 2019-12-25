#進位
def add(n):
    for i in range(n,0,-1):
        if num[i]==10:
            num[i]=0
            num[i-1]+=1
            p[i-1]=1

#上數
def up(n,count):
    for i in range(n+1):     
       if p[i]!=0:
          print(num[i],end="");
    print("")
    if num[n]!=10:
       num[n]+=1
    add(n)
    #判斷是否全為9
    if num[0]==10:
        num[0]=9
        for i in range(1,n+1):
            num[i]=9
        count=False
        return count
    return count

#借位
def sub(n,max):
    for c in range(n-1,-1,-1):
        if num[c]!=0:
            num[c]-=1
            for x in range(c+1,n+1):
                num[x]=9 
            #最高位數借完移至下一位    
            if(num[max]==0):               
                p[max]=0
                max+=1
                return max
            return max
            
#下數
def down(n,max,count):
    a=0
    if num[n]!=0:
        num[n]-=1

    #判斷是否全為0
    for i in range(n+1):
        a+=num[i]
    if a==0:
        for i in range(n):
            p[i]=0
        p[n]=1
        count=True
        max=0
        return count,max 
    
    #是否需要借位
    if num[n]==0:
        for i in range(n+1):
            if(p[i]!=0):
               print(num[i],end="")
        print("")
        max=sub(n,max)

    for i in range(n+1):
        if(p[i]!=0):
           print(num[i],end="")
    print("")
    return count,max  

#設定範圍
num=[0,0,0,0];#數值
p=[0,0,0,1];#顯示用
count=True
n=len(num)-1 
max=0

while(True):
    if count:
        count=up(n,count)
    else:
        count,max=down(n,max,count)