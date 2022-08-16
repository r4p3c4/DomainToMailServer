
# DomainToMailServer
DomainToMailServer is a module created for Spiderfoot, whose function is to obtain the mail servers corresponding to the domain you enter

# Requisitos y pasos a seguir

**Actualizas los paquetes:**

sudo apt-get update

<img src="https://i.postimg.cc/X7ctq845/1.jpg">

**Instalas python3 y pip3:**

sudo apt-get install python3-pip python3

<img src="https://i.postimg.cc/wBPGZ4cC/2.jpg">

**Instalas git:** 

sudo apt-get install git
<img src="https://i.postimg.cc/N0LnNvT8/3.jpg">

**Listas tu directorio actual y como por ejemplo accedes a la carpeta del escritorio con el comando cd Desktop:**

<img src="https://i.postimg.cc/YqwJtVKk/4.jpg">


**Te descargas el modulo DomainToMailServer:**

git clone https://github.com/r4p3c4/DomainToMailServer.git


<img src="https://i.postimg.cc/Xq6D7ZPx/5.jpg">

**Haces un ls para ver el contenido de la carpeta actual:**

<img src="https://i.postimg.cc/XYjmCCYz/6.jpg">


**Te descargas el programa de SpyderFoot:**

git clone https://github.com/smicallef/spiderfoot.git

<img src="https://i.postimg.cc/MTQFS09v/7.jpg">


**Haces un ls para ver el contenido de la carpeta actual:**

<img src="https://i.postimg.cc/P5Scz5Lr/8.jpg">


**Accedes a la carpeta creada de spiderfoot:**

cd spiderfoot/

<img src="https://i.postimg.cc/2jnK9wqt/9.jpg">


**Ejecutas el siguiente comando para instalar todas las dependencias para poder utilizar la herramienta de spiderfoot:**

sudo pip3 install -r requirements.txt

<img src="https://i.postimg.cc/tJdv1qQb/10.jpg">


**Copias el modulo DomainToMailServer en la carpeta de modulos de SpiderFoot:**

<img src="https://i.postimg.cc/c4Z5pnwL/11.jpg">


**Para ejecutar el programa**

python3 ./sf.py -l 127.0.0.1:3000

<img src="https://i.postimg.cc/k5kTf679/12.jpg">



**Al acceder verás la página principal:**
<img src="https://i.postimg.cc/3JBbYxFC/13.jpg">



**Accedes a new scan y pones un nombre al escaneo y el dominio que quieres escanear:**
<img src="https://i.postimg.cc/t4vSnvfs/14.jpg">


**Ahora seleccionas que el modo de escaneo va a ser por modulo y haces click en "De-select All" para desactivar todos los modulos:**

<img src="https://i.postimg.cc/Zq1p2nVL/15.jpg">


**Activas el modulo que hemos importado al programa:**

<img src="https://i.postimg.cc/TPyntgqw/16.jpg">


**A bajo del todo saldrá la opción Run Scan Now , y le haces click:**

<img src="https://i.postimg.cc/K8pn7JTw/17.jpg">


**Una vez finalizado el escaneo saldrá lo siguiente y le haces click en Email Gateway (DNS MX Records):**

<img src="https://i.postimg.cc/NMmmctnv/18.jpg">

**Ya nos mostrará los servidores de correo asociados al dominio que se ha puesto de ejemplo:**

<img src="https://i.postimg.cc/FzxGrT3s/19.jpg">





