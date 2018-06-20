#!/usr/bin/python3

import os

# Variáveis

rootdir = '/home/diogo.souza/migracao'
diretorio = []


# For para enntrar na pasta
for d in os.scandir('/home/diogo.souza/migracao'):
    if d.is_dir():
        for files in os.walk(d.path + '/network-script'):

# Função para coletar informações dos arquivos originais

def informacoes(nm_arq)

for arquivos in nm_arq:

info = []
lista = [ 'IPADDR=', 'NETMASK=', 'GATEWAY', 'DNS1']

with open (d.path + "/network-scripts" + nm_arq, "r") as arq_original
    for i in arq_original.readlines():
        for elemento in lista:
	    if elemento in i:
	        info.append(i)	    

# Escrever informações coletadas em um arquivo de texto

with open (d.path + "/network-scripts" + nm_arq_conv, "w+") as novo_arq
    for infos in lista:
        novo_arq.write(infos + '\n')

return True

