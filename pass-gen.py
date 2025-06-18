import random

print('Bem-vindo ao seu gerador de senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*(),.;<>:+=_-?0123456789'

number = int(input('Quantidade de senhas a serem geradas: '))
length = int(input('Insira quantos caracteres deseja para sua senha: '))

print('\nAqui estão suas senhas:')  # Caso gere mais de uma

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

input()
