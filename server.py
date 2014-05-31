 # -*- coding: utf-8 -*-
 #La ligne precedente permet l'utilisation des accents sans inquieter python


__author__ = 'Vincent Bathellier'

from os import popen
import psutil
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def chargeproc():
    """Fonction qui à pour but de recupèrer la charge du
    processeur et de la mettre dans un fichier html."""

    #récuperation de la charge du CPU
    # com = popen("wmic cpu get LoadPercentage /format:value")
    # result = com.readlines()
    # for lines in result:
    #     if lines != '\n':
    #         CPU = lines
    # CPU = CPU[15:]
    # chargeCPU = open("C:\Apache24\htdocs\chargecpu.html", "w")
    # chargeCPU.write(CPU)
    # print(CPU)
    # chargeCPU.close()

    #Recupere la charge pour chaque coeur du PC fonctionne sous
    #Windows, Linux, MacOSX, on preferera cette facon de faire
    #pour rendre le programme utilisable sous tout les OS.
    cpuloads = psutil.cpu_percent(0.0, True)
    #Affiche le resultat uniquement pour le fun et pour la partie educative
    print cpuloads

    #On verifie si au moins un processeur n'est pas trop utilisé, ici
    #inferieur a 10%, si oui on retourne True sinon on retourne False
    for cpuload in cpuloads:
        if cpuload < 10.0:
            return True
    return False

#Definition du main en python
if __name__ =='__main__':
    #creation d'un server JSONRPCServer
    server = SimpleJSONRPCServer(('localhost', 8080))
    #Indique que le client pourra appeler la fonction chargeproc
    server.register_function(lambda : chargeproc(), 'can_receive_task')
    #Demarrage du serveur qui fera aussi office de daemon
    server.serve_forever()
