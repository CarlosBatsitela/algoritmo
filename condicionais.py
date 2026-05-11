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
if numero2 >numero3 and numero2 >numero4:
    print(f'o maior é {numero2}')
elif numero3 >numero2 and numero3 >numero4:
    print(f'o maior é {numero3}')
else:
    print(f' o maior é {numero4} ')
#3,4

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
media=(nota1+nota2)/2
if media >=7:
    print('Aprovado')
else:
    print('Reprovado')
#5

idade=int(input('Digite sua idade: '))
if idade <18:
    print('Você é Criança')
elif idade <=60:
    print('Você é Adulto') 
else:   
    print('Você é Idoso')
#6

salario=float(input('Digite seu salário: '))
if salario >5000:
    print(f'seu desconto é {salario*0.9}')
else:
    print(f'seu desconto é {salario*0.95}')
#7

login=input('Digite seu login: ')
senha=input('Digite sua senha: ')
if login == 'admin' and senha == '1234':
    print('Acesso permitido')
else:
    print('Acesso negado')
#8

calculo1=float(input('Digite o primeiro numero: '))
operacao=input('Digite a operação: ')
calculo2=float(input('Digite o segundo numero: '))

if operacao == '+':
    print(f'Resultado: {calculo1 + calculo2}')
elif operacao == '-':
    print(f'Resultado: {calculo1 - calculo2}')
elif operacao == '*' or operacao == 'x':
    print(f'Resultado: {calculo1 * calculo2}')
elif operacao == '/' and calculo2 != 0:
    print(f'Resultado: {calculo1 / calculo2}')    
else:
    print('Operação inválida')
#9

altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
calculo=peso / (altura * altura)
if calculo <18.5:
    print('Abaixo do peso')
elif calculo <25:
    print('Peso normal')
elif calculo <30:
    print('Sobrepeso')
else:    
    print('Obesidade')
