import math
# variáveis numéricas
# com ponto decimal -> do tipo float
# sem ponto decimal -> int

# exemplo de int
# número de filhos
# número computadores
# dias até uma data
# dias num mês
# meses num ano
# quantidade de coisas que não são dividas

# programa para calcular quantos ônibus são 
# necessários para levar os golpistas para
# a prisão na PF ??
quantas = int(input("Quantas pessoas foram detidas?"))
# quantos ônibus serão necessários
# sabendo que cada cada ônibus cabe 40 pessoas
lotacao = 40 

# math.ceil -> arredonda para o próximo inteiro
# ou seja, arredonda para mais
quantosOnibus = math.ceil( quantas / lotacao )
print("Serão necessários ", quantosOnibus, "ônibus")
