nome = input("Qual é o seu nome?")
idade = input("Qual é a sua idade?")
cidade = input("Em que cidade você mora?")
peso = float(input("Quantos quilos você pesa?"))
altura = float(input("Qual é a sua altura em metros?"))

imc = peso / (altura * altura)

print("Seja bem vindo", nome)
print("Você tem", idade, "anos")
print("Você mora em",cidade)
print("O seu peso é", peso, "quilos")
print("A sua altura é",altura, "metros")
print("O seu IMC é",imc)

# input() sempre retorna uma string (texto)
# strings não podem ser usadas para cálculo
# para fazer cálculos com string é preciso converte-las
# para número (int ou float)
