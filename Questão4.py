print('Criador de gabarito:')
gabarito = []
listacertos = []
contador = 1
certa = '?'
menor = 11
maior = 0
outro = 's'
acertos = 0
while contador < 11:
    certa = str(input(f'Qual o gabarito da questão {contador}: '))
    gabarito.append(certa)
    contador += 1 
while outro == 's' or outro == 'S':
    acertos = 0
    print('Respostas dos alunos:')
    for i in range (len(gabarito)):
        resposta = input(f'Qual a resposta da questão {i+1}: ')
        if resposta == gabarito[i]:
            acertos += 1
    if acertos > maior: maior = acertos
    if acertos < menor: menor = acertos
    listacertos.append(acertos)
    print('Acertos contabilizados')
    outro = input('outro aluno vai ultilizar o sistema? (S / N)')
media = (sum(listacertos) / len(listacertos))
print(f'o maior acerto foi {maior}')
print(f'o menor acerto foi {menor}')
print(f'{len(listacertos)} alunos ultilizaram o sistema')
print(f'a medio dos alunos foi {media}')
print(listacertos)
