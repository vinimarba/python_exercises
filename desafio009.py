numero = int(input('Digite um número que deseja saber a tabuada: '))

#Sintaxe antiga (Python 2.7 e 3.0):

#print('{} x {:2} = {}'.format(numero, 2, numero*2))
#print('{} x {:2} = {}'.format(numero, 1, numero*1))
#print('{} x {:2} = {}'.format(numero, 3, numero*3))
#print('{} x {:2} = {}'.format(numero, 4, numero*4))
#print('{} x {:2} = {}'.format(numero, 5, numero*5))
#print('{} x {:2} = {}'.format(numero, 6, numero*6))
#print('{} x {:2} = {}'.format(numero, 7, numero*7))
#print('{} x {:2} = {}'.format(numero, 8, numero*8))
#print('{} x {:2} = {}'.format(numero, 9, numero*9))
#print('{} x {:2} = {}'.format(numero, 10, numero*10))

#Sintaxe atualizada (Python 3.6 >>):
print('-' * 15)
print(f'{numero} x {1:2} = {numero*1}')
print(f'{numero} x {2:2} = {numero*2}')
print(f'{numero} x {3:2} = {numero*3}')
print(f'{numero} x {4:2} = {numero*4}')
print(f'{numero} x {5:2} = {numero*5}')
print(f'{numero} x {6:2} = {numero*6}')
print(f'{numero} x {7:2} = {numero*7}')
print(f'{numero} x {8:2} = {numero*8}')
print(f'{numero} x {9:2} = {numero*9}')
print(f'{numero} x {10:2} = {numero*10}')
print('-' * 1)
#for count in range(10):
    #print("%d x %d = %d" % (numero, count+1, numero*(count+1)) )
#print('A tabuada do número {} é {}'.format(numero, resultado))