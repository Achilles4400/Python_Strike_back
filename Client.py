__author__ = 'Vincent Bathellier'
import http.client

def OpenIP(filename):
    file = open(filename,"r")
    for lignes in file:
        print("ligne :")
        print(lignes)
        ask(lignes)

def ask(addIP):
    askServ = http.client.HTTPConnection(addIP, 1025 )
    askServ.connect()
    askServ.request('GET',requete)
    chargeServ = askServ.getresponse()
    if chargeServ.status == httplibOK:
         printText(chargeServ.read())