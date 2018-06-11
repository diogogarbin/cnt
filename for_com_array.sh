#!/bin/bash -xv

#mkdir -p /home/diogo.souza/migracao

dic=( $(ls /var/rsync/bkp/ | grep lx) )
dic_length=${#dic[@]}
echo $dic


for i in ${dic[@]}; do
	if [ ! -d /var/rsync/bkp/$i/sysconfig/network-scripts ]; then
        
                mkdir -p /home/diogo.souza/migracao/$i

		chmod 755 /home/diogo.souza/migracao/

		cp -prf /var/rsync/bkp/$i/etc/sysconfig/network-scripts /home/diogo.souza/migracao/$i

	else

		touch /home/diogo.souza/migracao/erro_bkp.txt

		echo $i >> /home/diogo.souza/migracao/erro_bkp.txt

	fi

done




