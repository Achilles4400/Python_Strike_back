__author__ = 'Vincent Bathellier'

from os import popen
from time import sleep

#lancement du worker
#trouver ce qu'il faut mettre à la place de proj
#os.popen("celery -A Client worker --loglevel=info")


#fonction qui à pour but de recupèrer la charge du processeur et de la mettre dans un fichier html
def chargeproc():
    #récuperation de la charge du CPU
    com = popen("wmic cpu get LoadPercentage /format:value")
    result = com.readlines()
    for lines in result:
        if lines != '\n':
            CPU = lines
    CPU = CPU[15:]
    chargeCPU = open("C:\Apache24\htdocs\chargecpu.html","w")
    chargeCPU.write(CPU)
    chargeCPU.close()


#permet l'arrèt à la demande
encore = True
while encore:
    chargeproc()
    sleep(1)
