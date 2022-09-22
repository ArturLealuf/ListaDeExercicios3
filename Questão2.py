print('digite "0" para finalizar o pedido')
preçofinal = []
while True:
    item = int(input('Digite o codigo do item desejado: '))
    if item == 0: break
    qnt = int(input('qual a quantidade deste mesmo item você deseja: '))
    if item == 100 or item == 103:
        preço = 1.20
    elif item == 101 or item == 104:
        preço = 1.30
    elif item == 102:
        preço = 1.50
    elif item == 105:
        preço = 1
    else:
        print('item invalido')
    valor = preço * qnt
    preçofinal.append(valor)
valorfinal = sum(preçofinal)
print(f'o valor final se seu pedido é {valorfinal}')
