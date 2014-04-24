__author__ = 'Vincent Bathellier'
import http.client


#fonction qui récupére un stript à  éxecuter
def task():
    script = input("Entrez le script à éxécuter : ")
    file = open(script).read()
    print(file)

#fonction qui prend en paramètre une autre fonction
def api(taskToExecut):
    return taskToExecut()

#fonction qui récupére les adresse IP
def OpenIP(filename):
    file = open(filename,"r")
    for lignes in file:
        ask(lignes)

#fonction qui à pour but récupérer la charge des serveurs
def ask(addIP):
    askServ = http.client.HTTPConnection(addIP, 1025 )
    askServ.connect()
    askServ.request('GET',requete)
    chargeServ = askServ.getresponse()
    if chargeServ.status == httplibOK:
         printText(chargeServ.read())
