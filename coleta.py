#!/usr/bin/python3

import os
rootdir = '/home/diogo.souza/migracao'
diretorio = []
for d in os.scandir('/home/diogo.souza/migracao'):
    if d.is_dir():
        diretorio.append(d.path + '\n')
with open ('lista.tmp', 'a+') as lista:
    for y in diretorio:
        lista.write(y)

#info = []
#lista = [ 'IPADDR=' , 'NETMASK=' , 'GATEWAY=' , 'DNS1' ]
#with open ('ifcfg-em1' , 'r') as config:
#	
#	for i in config.readlines():
#	   for elemento in lista:
#	     if (elemento) in i:
#	        info.append(i)
#	print(info)
	
