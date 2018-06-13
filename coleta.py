#!/usr/bin/python

info = []
lista = [ 'IPADDR=' , 'NETMASK=' , 'GATEWAY=' , 'DNS1' ]
with open ('ifcfg-em1' , 'r') as config:
	
	for i in config.readlines():
	   for elemento in lista:
	     if (elemento) in i:
	        info.append(i)
	print(info)
	
