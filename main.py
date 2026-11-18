# 1. cadastro de usuário:
nome = str(input("Qual seu nome: "))
idade = int(input("Digite sua idade: "))
cidade = str(input("Onde você mora: "))

print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}.")

# 2. Conversor de temperatura:
celcius = float(input("Digite a temperatura atual em Celsius: °C "))
fahrenheit = (celcius * 9/5) + 32

print(f"Sua temperatura em Fahrenheit é °F{fahrenheit}.")

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

print(f"Resultado da divisão: {divisao:.2}. \nQuociente Inteiro: {quociente_inteiro}. \nResto da divisão {resto_da_divisao}.")

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

# 7. Análise de números
soma5 = 0

for i in range(0, 5):
    num5 = int(input("Digite um número: "))
    
    if i == 0:
        maior5 = num5
        menor5 = num5
    else:
        if num5 > maior5:
            maior5 = num5
        if num5 < menor5:
            menor5 = num5
            
    soma5 += num5

media5 = soma5 / 5

print(f"\nO maior número: {maior5}.")
print(f"O menor número: {menor5}.")
print(f"A soma dos números: {soma5}.")
print(f"A média: {media5}.")

# 8. Verificador de senha

senhaC = "python123"
senhaD = str(input("Digite sua senha: "))

if senhaD == senhaC :
    print("Acesso permitido.")
else:
    print("Acesso negado.")

# 9. Sistema de votação
votosM = 0
votosC = 0
votosA = 0

while True:
    voto = int(input("\nDigite o número do seu candidato:\n1. Murilo\n2. Caio\n3. André\n0. Fechar urna\n"))

    if voto == 1:
        votosM += 1
    elif voto == 2:
        votosC += 1
    elif voto == 3:
        votosA += 1
    elif voto == 0:
        break
    else:
        print("Opção inválida! Tente novamente.")

print(f"\nVotos Murilo: {votosM}.")
print(f"Votos Caio: {votosC}.")
print(f"Votos André: {votosA}.")

# 10. Controle de compras
precos = []

for i in range(5):
    preco = float(input(f"Digite o preço do {i+1}º produto: R$ "))
    precos.append(preco)

total = sum(precos)
mais_caro = max(precos)
media = total / len(precos)

print("\n--- Resumo da Compra ---")
print(f"Todos os preços: {precos}")
print(f"Valor total da compra: R$ {total:.2f}")
print(f"Produto mais caro: R$ {mais_caro:.2f}")
print(f"Média dos preços: R$ {media:.2f}")
