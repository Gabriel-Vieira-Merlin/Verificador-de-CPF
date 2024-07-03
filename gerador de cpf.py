#Declara as variáveis
import random

novedig = 0
cpf = 0
multi = 10
soma = 0

#Gera 9 números aleatórios
novedig = random.randint(10000000, 999999999)
print(novedig)

#Transforma os 9 dígitos em str para ele ser iterável
novedig = str(novedig)

#Calculam o primeiro digito
for num in novedig:
    soma = soma + int(num) * multi
    multi -= 1

#Multiplica a soma por 10
res = soma * 10

#Pega o resto da soma dividido por 11
dig1 = res % 11

#Faz uma condição que caso o valor seja maior que 9, ele se torna 0
if dig1 > 9:
    dig1 = 0

#Transforma os nove dígitos e o resultado em str para mesclar os dois números e depois prosseguir com as operações
dezdig = str(novedig) + str(dig1)

#Transforma o multiplicador em 11 e a soma em 0
multi = 11
soma = 0

#Calcula o segundo digito
for num in dezdig:
    soma = soma + int(num) * multi
    multi -= 1

#Multiplica a soma por 10
res = soma * 10

#Pega o resto da soma dividido por 11
dig2 = res % 11

#Faz uma condição que caso o valor seja maior que 9, ele se torna 0
if dig2 > 9:
    dig2 = 0

#Transforma os dex dígitos e o resultado em str para mesclar os dois números para formar o cpf
onzedig = str(dezdig) + str(dig2)
print(onzedig)