#!/usr/bin/python

with open('ifcfg-enp0s20u4', "a+") as arq:
	for i in arq.readlines():
	    conteudo = i
#	    print(conteudo)
with open ('testando.txt' , 'w+') as novo:
	for i in novo.readlines():
	    conteudo.replace('yes' , 'talvez')
	    conteudo = conteudo	
	    novo.append(conteudo)
