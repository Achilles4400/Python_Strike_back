 # -*- coding: utf-8 -*-
__author__ = 'Vincent Bathellier'

import Client
from celery import Celery

#choix du serveur sur lequel nous allons envoyer
fileIP = input("Entrez le fichier d'adresse IP : ")
host = Client.openIP(fileIP)
tache = Celery('tasks', broker='amqp://guest:guest@'+host+':5672//')


@tache.task
#fonction qui va contenir le code à exécuter
def funcret(file):
    return eval(file)
