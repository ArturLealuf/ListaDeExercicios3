print('Defeitos:\n1 - Necessita de Esfera\n2 - Necessita de limpeza')
print('3 - Necessita troca de cabo ou conector \n4 - Quebrado ou inutilizado')
quantidade = 0
d1 = []
d2 = []
d3 = []
d4 = []
while True:
    situação = int(input('qual a situação do mouse: '))
    if situação == 0: break
    elif situação == 1: d1.append(situação)
    elif situação ==  2: d2.append(situação)
    elif situação ==  3: d3.append(situação)
    elif situação ==  4: d4.append(situação)
    else:print('numero invalido, tente novamente')
    quantidade +=1
print(f'quantidades de mouses: {quantidade}')
print(' situação                                      quantidade      percentual ')
print(f'1 - Necessita de Esfera                         {len(d1)}               {(len(d1)/quantidade) * 100}%')
print(f'2 - Necessita de limpeza                        {len(d2)}               {(len(d2)/quantidade) * 100}%')
print(f'3 - Necessita troca de cabo ou conector         {len(d3)}               {(len(d3)/quantidade) * 100}%')
print(f'4 - Quebrado ou inutilizado                     {len(d4)}               {(len(d4)/quantidade) * 100}%')