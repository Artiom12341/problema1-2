b=list(input('Dati numarul='))
for i in range(0, len(b)): 
    b[i] = int(b[i])
s=0
c=0
for a in range(0,len(b)):
    if a%2==0:
        s+=1
    else:
        s=s+0
    if a%2!=0:
        c+=1
    else:
        c+=0
print('numarul de cifre pare=',s,'numarul de cifre impare=',c) 