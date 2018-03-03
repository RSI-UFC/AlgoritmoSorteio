# -*- coding: utf-8 -*-
from os import system
from random import randint, seed

#Comando para limpar a tela
system("reset")

#Configurar o Programa
semente_sorteio = int(input("Entre com o valor da semente: "))
numero_de_sorteios = int(input("Entre com o número de sorteios: "))
nome_arquivo = input("Entre com o caminho para o arquivo: ")

#Carrega a chave
seed(semente_sorteio)

lista_participantes = []
lista_sorteados = []

#Carrega nome dos participantes dentro de uma lista
lista_participantes = [line.rstrip('\n') for line in open(nome_arquivo)]

#Realiza os Sorteios
for i in range(0, numero_de_sorteios):
    lista_sorteados.append(lista_participantes.pop(randint(0, len(lista_participantes) - 1)))

#Comando para limpar a tela
system("reset")

#Mostra o nome dos sorteados
print("Ganhador(es) do Sorteio:")
for i in range(len(lista_sorteados)):
    print(lista_sorteados[i])

print("\nParabéns!!!")
input()

