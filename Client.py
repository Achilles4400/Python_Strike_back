__author__ = 'Vincent Bathellier'
import http.client
from celery import Celery

#fonction qui récupére un stript à  éxecuter
def task():
    script = input("Entrez le script à éxécuter : ")
    file = open(script).read()
    print(file)

#fonction qui prend en paramètre une autre fonction et qui retourne le resultat
def api(taskToExecut):
    fileIP = input("Entrez le fichier d'adresse IP : ")
    host = OpenIP(fileIP)
    app = Celery(taskToExecut, broker='amqp://guest:'+host+':1024//')


#fonction qui récupére les adresse IP et qui renvoi une adresse IP
def OpenIP(filename):
    file = open(filename,"r")
    for lignes in file:
        IP = lignes
        charge = ask(lignes)
    return IP

#fonction qui à pour but récupérer la charge des serveurs
def ask(addIP):
    askServ = http.client.HTTPConnection(addIP, 1025 )
    askServ.connect()
    askServ.request('GET',requete)
    chargeServ = askServ.getresponse()
    if chargeServ.status == httpOK:
         return(chargeServ.read())