saltos = []
while True:
    atleta = input('qual o nome do atleta: ')
    if atleta == '': break
    for i in range(5):
        salto = float(input('qual a distancia dos saltos: '))
        saltos.append(salto)
    print(f'Atleta:             {atleta}')
    print(f'Primeiro salto:          {saltos[0]}m')
    print(f'Segundo salto:          {saltos[1]}m')
    print(f'Terceiro salto:          {saltos[2]}m')
    print(f'Quarto salto:          {saltos[3]}m')
    print(f'Quinto salto:          {saltos[4]}m')
    print(f'\nmelhor salto :            {max(saltos)}m')
    print(f'menor salto:            {min(saltos)}m')
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    media = sum(saltos) / len(saltos)
    print(f'media dos demais saltos:            {media}m')
    print(f'resultado final: \n{atleta}: {media}m')
