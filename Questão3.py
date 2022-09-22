votos = []
print('Codigos de votação:\nLula : 1\nBolsonaro : 2\nCiro Gomes : 3\nSimone Tebet : 4')
print('voto nulo : 5\nvoto em branco : 6\nfinalizar a votação: 0')
while True:
    voto = int(input('em quem você quer votar: '))
    if voto == 0: break
    votos.append(voto)
pctnull = votos.count(5) / (len(votos) / 100)
pctbranco = votos.count(6) / (len(votos) / 100)
print(f'Lula teve {votos.count(1)} votos')
print(f'Bolsonaro teve {votos.count(2)} votos')
print(f'Ciro gomes teve {votos.count(3)} votos')
print(f'Simone Tebet teve {votos.count(4)} votos')
print(f'Nesta votação tiveram {votos.count(5)} votos nulos')
print(f'Nesta votação tiveram {votos.count(6)} votos em branco')
print(f'os votos nulos equivaleram a {pctnull}% da votação, já os votos em branco equivaleram a {pctbranco}%')
