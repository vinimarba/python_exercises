carteira = float(input('Digite a seguir o valor que você tem em carteira: R$'))
conversao = carteira*5.77

#print('{} em carteira equivale a {} dólares'.format(carteira, conversao))

print(f'R${carteira} em carteira equivale a US${conversao:.2f}.')
