# Scrapy Python web El Tenedor vs dataset Airbnb
Usamos la librería <a href="https://scrapy.org/">Scrapy</a> en Python para cruzar los datos de los alojamientos del dataset de <a href="https://public.opendatasoft.com/explore/dataset/airbnb-listings/export/?disjunctive.host_verifications&disjunctive.amenities&disjunctive.features&q=Madrid&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6Imhvc3RfbGlzdGluZ3NfY291bnQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiJyYW5nZS1jdXN0b20ifV0sInhBeGlzIjoiY2l0eSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJyb29tX3R5cGUiLCJjb25maWciOnsiZGF0YXNldCI6ImFpcmJuYi1saXN0aW5ncyIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUuaG9zdF92ZXJpZmljYXRpb25zIjp0cnVlLCJkaXNqdW5jdGl2ZS5hbWVuaXRpZXMiOnRydWUsImRpc2p1bmN0aXZlLmZlYXR1cmVzIjp0cnVlfX19XSwidGltZXNjYWxlIjoiIiwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D&location=16,41.38377,2.15774&basemap=jawg.streets">Airbnb</a> con la web de <a href="https://www.eltenedor.es/">El Tenedor</a> para encontrar restaurantes cerca de los alojamientos.

El cruce genera un fichero csv de los restaurantes cercanos a cada alojamiento. La siguiente parte constará de subir ambos ficheros (csv Airbnb + csv Scrapy) al clúster de Hadoop para el procesamiento de los datos.

## Comenzando 🚀
Estas instrucciones te permitirán obtener una copia del proyecto para hacer pruebas siguiendo las instrucciones que se detallan a continuación.

Este proyecto es un ejercicio que forma parte de la práctica que tuve que realizar para el módulo de Big Data Architecture en el bootcamp que cursé en KeepCoding sobre Big Data & Machine Learning, pero te puede servir para aprender conceptos básicos de Python y Scrapy.

### Pre-requisitos 📋
- Python3
- <a href="https://pypi.org/project/pip/">pip</a> (Gestor de paquetes para instalar Scrapy)
- <a href="https://scrapy.org/">Scrapy</a> (Librería para poder hacer crawling y scrapping con Python)
- CSV Dataset Airbnb (se adjunta un fichero pequeño para hacer las pruebas)

### Instalación 🔧
**Para instalar Python3:**

Basta con ir a la <a href="https://www.python.org/downloads/">web de descargas de Python</a> y descargar la correspondiente a tu sistema operativo.

**Para instalar pip (Mac OS):**

```
sudo easy_install pip
```

```
sudo pip install --upgrade pip
```

**Para instalar Scrapy (Mac OS):**

```
pip install scrapy
```

### Probando el proyecto ⚙️
 En el fichero **config.py** podemos ver la configuración necesaria para que el programa funcione, ahí deberemos configurar la ruta donde tenemos el csv del dataset de Airbnb si queremos cambiarlo y usar otro diferente al que se adjunta.

 En el repositorio se incluye el fichero **scrap.sh** llamando a este script desde la terminal de Mac OS se ejecutará el programa en python que obtendrá un csv con todos los restaurantes cercanos a cada apartamento que haya en el dataset de Airbnb. La forma de ejecutar el scrip desde la terminal es:

```
./scrap.sh
``` 

**Importante tener instalado python3. El script dejará un nuevo csv con el resultado del cruce en la carpeta del proyecto, si se desea cambiar el dataset, habrá que cambiar también la ruta en la configuración o usar el mismo nombre y ruta del que se adjunta como ejemplo.**

Para el ejemplo nos vamos a centrar solo en restaurantes cuyo código de país sea España (ES). Este punto está parametrizado en el fichero de configuración, si no deseamos filtrado por país basta con poner el carácter '*' en el filtro de país.

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓
* Sígueme en <a href="https://twitter.com/AsensiFj">Twitter</a> 🐦
