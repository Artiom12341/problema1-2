b=list(input('Dati numarul='))
for i in range(0, len(b)): 
    b[i] = int(b[i])
for a in range(len(b)):
    if int(b[i-1]) <int(b[i]):
        print('numerele sunt  ord. str .crescator',b)
    else:
        print('numerele nu sunt  ord. str .crescator',b)