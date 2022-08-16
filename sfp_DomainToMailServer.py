# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        DomainToMailServer
# Purpose:     Obtiene los servidores de correo a traves del dominio que indiques
#
# Author:      Rafael Peiro Calvet <rafaelpeiro27@gmail.com>
#
# Created:     16/08/2022
# Copyright:   (c) Rafael Peiro Calvet 2022
# Licence:     GPL
# -------------------------------------------------------------------------------


from spiderfoot import SpiderFootEvent, SpiderFootPlugin
import subprocess
#pones el mismo nombre en la clase que en el nombre del modulo.py
class sfp_DomainToMailServer(SpiderFootPlugin):

    meta = {
        'name': "DomainToMailServer",
        'summary': "Obtiene los servidores de correo a traves del dominio que indiques",
        'flags': [""],
        'useCases': [""],
        'categories': ["Passive DNS"]
    }

    # Default options
    opts = {
    }

    # Option descriptions
    optdescs = {
    }

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    #Para averiguar que hay que poner en el return hay que ir a la carpeta spiderfoot --> db.py 
    
    # Aqui pones el dato de entrada, que en mi caso voy a poner un dominio
    def watchedEvents(self):
        return ["DOMAIN_NAME"]

    #Aqui pones el dato de salida, que es el resultado que nos va a proporcionar 
    #En mi caso quiero ver los servidores de correos realacionados con el dominio que he puesto anteriormente
    def producedEvents(self):
        return ["PROVIDER_MAIL"]

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if eventData in self.results:
            return

        self.results[eventData] = True

        self.sf.debug(f"Received event, {eventName}, from {srcModuleName}")

        try:
            self.sf.debug(f"We use the data: {eventData}")
            print(f"We use the data: {eventData}")

            ########################
            # Insert here the code #
            ########################
            
           #evenTData es el parametro de entrada que mete el usuario
           #Lo que está ejecutando el subprocess es que va a obtener los servidores de correo 
           # relacionados con el dominio que le pongas, y para que solo te muestre los servidores de correo
           #con awk seleccionas la septima columna y asi obtenemos solo los servidores de correo 
        
            data=subprocess.run("host -t MX "+eventData+"|awk '{print $7}'",shell=True,text=True,capture_output=True)

            serv_correo=data.stdout
            
            ########################

            #Si se produce algun error te lo va a indicar

            if not serv_correo:
                self.sf.error("Unable to perform <ACTION MODULE> on " + eventData)
                return
        except Exception as e:
            self.sf.error("Unable to perform the <ACTION MODULE> on " + eventData + ": " + str(e))
            return

#Con estas lineas ya devolvemos el resultado de la ejecucion del modulo    
     
#PROVIDER_MAIL es el tipo dato que se ha seleccionado anteriormente de la BD, 
# y serv_correo es la variable que tiene el resultado obtenido"
        evt = SpiderFootEvent("PROVIDER_MAIL",serv_correo, self.__name__, event)
        self.notifyListeners(evt)

# End of sfp_DomainToMailServer class