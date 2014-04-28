__author__ = 'Vincent Bathellier'

import os
from flask import Flask


apli = Flask()


#fonction qui à pour but de recupèrer la charge du processeur et de la mettre dans un fichier html
@apli.route("C:\web")
def chargeproc():
    #récuperation de la charge du CPU
    CPU = os.system("wmic cpu get LoadPercentage /format:value")
    CPU = str(CPU)
    chargeCPU = open("chargecpu.html","w")
    chargeCPU.write(CPU)
    chargeCPU.close()

apli.run()

