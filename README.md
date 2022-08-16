
# DomainToMailServer
DomainToMailServer is a module created for Spiderfoot, whose function is to obtain the mail servers corresponding to the domain you enter

# Requisitos y pasos a seguir

Actualizas los paquetes

sudo apt-get update

<img src="https://i.postimg.cc/X7ctq845/1.jpg">

Instalas python3 y pip3
sudo apt-get install python3-pip python3

<img src="https://i.postimg.cc/wBPGZ4cC/2.jpg">

Instalas git 

sudo apt-get install git
<img src="https://i.postimg.cc/N0LnNvT8/3.jpg">

Listas tu directorio actual y como por ejemplo accedes a tu escritorio
Lo listas con el comando ls

<img src="https://i.postimg.cc/YqwJtVKk/4.jpg">


Accedes a la carpeta del escritorio con el comando cd Desktop
<img src="https://i.postimg.cc/Xq6D7ZPx/5.jpg">




Te descargas el modulo DomainToMailServer

git clone https://github.com/r4p3c4/DomainToMailServer.git

Haces un ls para ver el contenido de la carpeta actual




Te descargas el programa de SpyderFoot

git clone https://github.com/smicallef/spiderfoot.git

Haces un ls para ver el contenido de la carpeta actual


Accedes a la carpeta creada de spiderfoot

cd spiderfoot/

Ejecutas el siguiente comando para instalar todas las dependencias para poder utilizar la herramienta de spiderfoot

sudo pip3 install -r requirements.txt


Copias el modulo DomainToMailServer en la carpeta de modulos de SpiderFoot







Para ejecutar el programa 

python3 ./sf.py -l 127.0.0.1:3000



