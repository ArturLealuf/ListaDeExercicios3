salarios = []
abonos = []
while True:
    salario = int(input('Qual o seu salario bruto: '))
    if salario == 0: break
    abono = (salario * 20) / 100
    if abono < 100: abono = 100
    salarios.append(salario)
    abonos.append(abono)
for i in range(len(salarios)):
    print('salario: ',salarios[i], '        abono:', abonos[i])
print(f'foram processados {len(salarios)} colaboradores')
print(f'total gasto com abonos: R${sum(abonos)}')
print(f'{abonos.count(100)} pessoas receberam o abono minimo')
print(f'maior valor pago com abono: R${max(abonos)}')
