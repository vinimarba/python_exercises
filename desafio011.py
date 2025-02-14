input('Bem-vindo!')
largura = float(input('Digite a largura da parede (metros): '))
altura = float(input('Agora digite a altura da parede (metros): '))
area = largura*altura
tinta = area/2

#print('A área total é de {} metros quadrados. Para pintar, seria necessário {} litros de tinta'.format(area, tinta))

print(f'A área total é de {area} metros quadrados. Para pintar, seriam necessários {tinta} litros de tinta.')