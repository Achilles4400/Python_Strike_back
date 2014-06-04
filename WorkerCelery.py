 # -*- coding: utf-8 -*-
__author__ = 'Vincent Bathellier'

import Client
from celery import Celery

#choix du serveur sur lequel nous allons envoyer

# Ceci est cote serveur il ne faut donc pas demander l'IP ici !
# fileIP = input("Entrez le fichier d'adresse IP : ")
# host = Client.openIP(fileIP)

tache = Celery('tasks', broker='amqp://guest:guest@localhost:5672//', backend='amqp')


@tache.task
#fonction qui va contenir le code à exécuter
def funcret(file):
    return eval(file)

@tache.task
def run_func(source):
    res = {}
    exec(source) in res
    return res["return_value"]
