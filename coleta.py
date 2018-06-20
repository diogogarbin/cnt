#!/usr/bin/python3

import os
letra = 'teste'
rootdir = '/home/diogo.souza/migracao'
diretorio = []
#teste = teste_arq
for d in os.scandir('/home/diogo.souza/migracao'):
    if d.is_dir():
        print(d.path)
        with open(d.path + "/teste","a+") as arquivo:
            arquivo.write(letra + '\n')

#        diretorio.append(d.path + '\n')
#with open ('lista.tmp', 'a+') as lista:
#    for y in diretorio:
#        lista.write(y)
#
#info = []
#lista = [ 'IPADDR=' , 'NETMASK=' , 'GATEWAY=' , 'DNS1' ]
#with open ( d.path , 'r') as config:
#	
#	for i in config.readlines():
#	   for elemento in lista:
#	     if (elemento) in i:
#	        info.append(i)
#	print(info)
	
