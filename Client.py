__author__ = 'Vincent Bathellier'
import http.client
from celery import Celery

fileIP = input("Entrez le fichier d'adresse IP : ")
host = OpenIP(fileIP)
tache = Celery(taskToExecut, broker='amqp://guest:'+host+':1024//')

#fonction qui récupére un stript à  éxecuter
@tache.task
def fonc():
    script = input("Entrez le script à éxécuter : ")
    file = open(script).read()

#fonction qui prend en paramètre une autre fonction et qui retourne le resultat
def api(fonc):
    result = fonc.delay(4,4)
    return result.get()


#fonction qui récupére les adresse IP et qui renvoi une adresse IP
def OpenIP(filename):
    global IPviable
    file = open(filename,"r")
    for lignes in file:
        IPviable = lignes
        charge = ask(lignes)
    return IPviable

#fonction qui à pour but récupérer la charge des serveurs
def ask(addIP):
    askServ = http.client.HTTPConnection(addIP, 1025 )
    askServ.connect()
    askServ.request('GET','index.html')
    chargeServ = askServ.getresponse()
    if chargeServ.status == 200: #200 correspond au status OK
         return (chargeServ.read())