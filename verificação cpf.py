#Variáveis que serão usadas
multi = 10 #Multiplicador que será usado para multiplicar os 9 primeiros dígitos do cpf
cpf = '' #Cpf que será digitado pelo usuário
soma = 0 #Soma de cada número pelo multiplicador
dig1 = 0 #Primeiro digito do CPF
dig2 = 0 #Segundo dígito do CPF

#Cria um while que coleta o CPF e verifica que possui a quantidade de números correta
while True:
    cpf = input('Digite o CPF: ')
    if len(cpf.strip()) == 11:
        print('REALIZANDO A VERIFICAÇÃO')
        break
    else:
        print('FOI DIGITADO MAIS CARACTERES QUE O PERMITIDO, DIGITE NOVAMENTE: ')

#Faz um for para os 9 primeiros digitos do cpf
for num in cpf[:9]:
    soma = soma + int(num) * multi
    multi -= 1

#Multiplicação da soma por 10
resultado = soma * 10

#Coleta o resto da divsão da soma por 11
dig1 = resultado % 11

#Condição para verificar o valor do 1° digito do cpf, no caso se o resultado for maior que 9, o digito se torna 0
if dig1 > 9:
    dig1 = 0

#Printando o primeiro digito
print(f'O primeiro digito do CPF é: {dig1}')

#Calculando o 2° digito

#Definindo o multiplicador como 11 e a soma como 0
multi = 11
soma = 0

#Multiplica os 9 números e o primeiro digite e depois soma
for num in cpf[:10]:
    soma = soma + int(num) * multi
    multi -= 1

#Multiplicação da soma por 10
resultado = soma * 10

##Coleta o resto da divsão da soma por 11
dig2 = resultado % 11

#Condição para verificar o valor do 1° digito do cpf, no caso se o resultado for maior que 9, o digito se torna 0
if dig2 > 9:
    dig2 = 0

#Printando o segundo digito
print(f'O segundo digito do CPF é: {dig2}')

#Verifica se o CPF é válido
if int(cpf[-2]) == dig1 and int(cpf[-1]) == dig2:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')