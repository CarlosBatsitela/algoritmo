numero=float(input('Digite um numero: '))

if numero >0:
    print('O numero é positivo')
elif numero <0:
    print('O numero é negativo')
else:
    print('O numero é zero')
#1

numero1=float(input('Escolha um numero: '))

if numero1 % 2 ==0:
    print('O numero é par')
else:
    print('O numero é impar')
#2

numero2=float(input('digite um numero: '))
numero3=float(input('digite mais um numero: '))
numero4=float(input('digite o ultimo numero: '))
if numero2 >numero3:
    print('o maior é {numero2}')
else:
    print('o maior é {numero3}')
#3,4

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
media=({nota1}+{nota2})/2
if media >=7:
    print('Aprovado')
else:
    print('Reprovado')
#5

idade=int(input('Digite sua idade: '))
if idade <=18:
    print('Você é Criança')
elif idade <=60:
    print('Você é Adulto') 
else:   
    print('Você é Idoso')
#6

salario=float(input('Digite seu salário: '))
if salario >5000:
    print('{salario}*0.9')
else:
    print('{salario}*0.95')
#7

login=input('Digite seu login: ')
senha=input('Digite sua senha: ')
if login == 'admin' and senha == '1234':
    print('Acesso permitido')
else:
    print('Acesso negado')
#8

