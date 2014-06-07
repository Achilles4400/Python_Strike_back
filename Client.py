 # -*- coding: utf-8 -*-
__author__ = 'Vincent Bathellier'

import jsonrpclib


def ask(addressIP):
    print ("scanning " +addressIP)
    import signal

    def timeout():
        raise Exception("timeout")

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(5)
    try:
        addressIP = addressIP.replace('\n','')

        server = jsonrpclib.Server('http://'+ str(addressIP) +':8080')
        charge = server.can_receive_task()

        if charge:
            print("Serveur is OK for computing")
        else:
            print("Serveur is non-OK for computing")
        signal.alarm(0)
        return charge
    except Exception as e:
        return False


#fonction qui récupére les adresse IP et qui renvoi une adresse IP
def openIP(filename):
    global IPviable
    chargeserv = 100
    file = open(filename, "r")
    for lines in file:
        charge = ask(lines)
        print (lines + " charge: " + str(charge))
        if charge is False:
            continue
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



def api_call_code(code):
    good_ip = openIP("addIP.txt")
    from celery import Celery
    if not good_ip:
        return "ERROR 1: no server avaiable!!"
    print (good_ip)

    my_celery = Celery(broker="amqp://guest:guest@"+good_ip+":5672//", backend="amqp")
    return my_celery.send_task("WorkerCelery.run_func", (code,))


# @celery.task
# #fonction qui prend en paramètre une autre fonction et qui retourne le resultat
# def api():
#     file = func()
#     result = WorkerCelery.funcret(file).delay(4, 4)
#     return result.get()


