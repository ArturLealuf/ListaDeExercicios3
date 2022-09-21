num = 0
a = []
b = []
c = []
d = [] 
while num >= 0:
    num = int(input('insira um número: '))
    if num < 26:
        a.append(num)
    elif num < 51:
        b.append(num)
    elif num < 76:
        c.append(num)
    elif num < 101:
        d.append(num)
print(f'total de numeros de 0-25 = {len(a) - 1}, de 26-50 = {len(b)}, de 51-75 = {len(c)}, de 76 - 100 = {len(d)}')