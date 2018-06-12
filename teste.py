#!/usr/bin/python

with open('ifcfg-em1', "a+") as arq:
	for i in arq.readlines():
            i = i.replace('yes' , 'talvez')
	    conteudo = i
            print(conteudo)
with open ('testando.txt' , 'w+') as novo:
	for x in conteudo:
	    novo.writelines(conteudo)
	
