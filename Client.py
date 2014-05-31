 # -*- coding: utf-8 -*-
__author__ = 'Vincent Bathellier'

import urllib2
import WorkerCelery
import celery
import jsonrpclib



def ask(addressIP):
    global charge
    server = jsonrpclib.Server('http://' + addressIP + ':8080')
    charge = server.can_receive_task()
    if charge:
        print("Serveur is OK for computing")
    else:
        print("Serveur is non-OK for computing")
    return charge



# #fonction qui à pour but récupérer la charge des serveurs
# def ask(addressIP):
#     askserv = http.client.HTTPConnection(addressIP, 5000)
#     askserv.connect()
#     askserv.request('GET', "chargeCPU.html")
#     charge = askServ.getresponse()
#     if charge.status == 200:  #200 correspond au status OK
#         return charge.read()



#fonction qui récupére les adresse IP et qui renvoi une adresse IP
def openIP(filename):
    global IPviable
    chargeserv = 100
    file = open(filename, "r")
    for lines in file:
        charge = ask(lines)
        #on prend la machine qui à le processeur le moins chargé
        if chargeserv >= charge:
            chargeserv = charge
            IPviable = lines
    file.close()
    return IPviable


#fonction qui récupére un stript à  éxecuter
def func():
    script = input("Entrez le script à éxécuter : ")
    file = open(script).read()
    return file


@celery.task
#fonction qui prend en paramètre une autre fonction et qui retourne le resultat
def api():
    file = func()
    result = WorkerCelery.funcret(file).delay(4, 4)
    return result.get()