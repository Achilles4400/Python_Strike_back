__author__ = 'Vincent Bathellier'

import http.client

from celery import Celery


fileIP = input("Entrez le fichier d'adresse IP : ")
host = openIP(fileIP)
tache = Celery('tasks', broker='amqp://guest:' + host + ':1025//')


#fonction qui à pour but récupérer la charge des serveurs
def ask(addressIP):
    askserv = http.client.HTTPConnection(addressIP, 5000)
    askserv.connect()
    askserv.request('GET', "chargeCPU.html")
    charge = askServ.getresponse()
    if charge.status == 200:  #200 correspond au status OK
        return charge.read()


#fonction qui récupére les adresse IP et qui renvoi une adresse IP
def openIP(filename):
    global IPviable
    file = open(filename, "r")
    #à modifier : TQ charge sup à val on cherche un autre serveur
    for lines in file:
        IPviable = lines
        charge = ask(lines)
    file.close()
    return IPviable


#fonction qui récupére un stript à  éxecuter
def func():
    script = input("Entrez le script à éxécuter : ")
    file = open(script).read()
    return file


@tache.task
#fonction qui va contenir le code à exécuter
def funcret(file):
    return eval(file)

@celery.task
#fonction qui prend en paramètre une autre fonction et qui retourne le resultat
def api():
    file = func()
    result = funcret(file).delay(4, 4)
    return result.get()