# 1. cadastro de usuário:
nome = str(input("Qual seu nome: "))
idade = int(input("Digite sua idade: "))
cidade = str(input("Onde você mora: "))

print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}.")

# 2. Conversor de temperatura:
celcius = float(input("Digite a temperatura atual em Celsius: °C "))
fahrenheit = (celcius * 9/5) + 32

print(f"Sua temperatura em Fahrenheit é °F{fahrenheit}")

# 3. Calculadora de tempo:
minutos = int(input("Digite uma quantidade em minutos: "))
horas = minutos / 60

print(f"Convertendo para horas você tem {horas:.2} horas.")

# 4. Divisão de valores:
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
divisao = numero1 / numero2
quociente_inteiro = numero1 // numero2
resto_da_divisao = numero1 % numero2

print(f"Resultado da divisão: {divisao:.2}. \nQuociente Inteiro: {quociente_inteiro}. \nResto da divisão {resto_da_divisao}")

# 5. Ingresso cinema:
idade2 = int(input("Digite sua idade: "))

if idade2 < 12 :
    print("Você pagará R$10,00.")
elif idade2 >= 12 and idade2 <= 17 :
    print("Você pagará R$15,00.")
else:
    print("Você pagará R$25,00.")

# 6. Contagem personalizada:
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

for i in range(num1, num2) :
    print(i)