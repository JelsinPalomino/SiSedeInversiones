
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!-- *** https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[![Build-sphinx-docs][Build-sphinx-docs-shield]][Build-sphinx-docs-url]
[![Test-Linters-Publish][Test-Linters-Publish-shield]][Test-Linters-Publish-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Contributors][contributors-shield]][contributors-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Download-PyPi][downloads-PyPi-shield]][downloads-PyPi-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JelsinPalomino/SiSedeInversiones">
    <img src="images/logo4.png" alt="Logo" width="80" height="80" style="border-radius: 10px;">
  </a>

<h3 align="center">SiSedeInversiones</h3>

  <p align="center">
    Este paquete está dedicado a automatizar la recolección de datos que se encuentran en el portal “Sistema de Seguimiento de Inversiones – SSI” del Estado peruano, donde se pueden monitorear los proyectos de inversión pública en el Perú a través de los Códigos Únicos de Inversión (CUI).
    <br />
    <a href="https://jelsinpalomino.github.io/SiSedeInversiones/"><strong>Ir a la Documentación »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    &middot;
    <a href="https://github.com/JelsinPalomino/SiSedeInversiones/issues/new?template=bug-report.md">Report Bug</a>
    &middot;
    <a href="https://github.com/JelsinPalomino/SiSedeInversiones/issues/new?template=feature-request.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del proyecto</a>
      <ul>
        <li><a href="#construido-con">Construido con</a></li>
      </ul>
    </li>
    <li>
      <a href="#empezando">Empezando</a>
      <ul>
        <li><a href="#pre-requisitos">Pre-requisitos</a></li>
        <li><a href="#instalacion">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <!-- <li><a href="#roadmap">Hoja de ruta</a></li> -->
    <li><a href="#contribuyendo">Contribuyendo</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <!-- <li><a href="#acknowledgments">Agradecimientos</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

![image](images/logo.jpg)

**SiSedeInversiones**, es un paquete de python diseñada para automatizar la tarea de recolectar información de los proyectos de inversión pública de Perú que se encuentran en el "Sistema de Seguimiento de Inversiones (SSI)".
<br>
<br>
SiSedeInversiones hace uso de los Códigos Únicos de Inversiones (CUI) de los proyectos de inversión para realizar la consulta en el portal del SSI, de donde extrae la información sobre los:

* Datos generales
* Información financiera
* Contratos
* InfObras

Asimismo, también puede recolectar la información de los proyectos, que se encuentran en el:

* Formato N°08-A Registros en la Fase de Ejecución <a href="https://ofi5.mef.gob.pe/invierte/ejecucion/verFichaEjecucion/2562741">Ejemplo</a>
* La lista de ejecución simple pública. <a href="https://ofi5.mef.gob.pe/invierte/ejecucion/traeListaEjecucionSimplePublica/2562741">Ejemplo</a>

En ese sentido, **SiSedeInversiones** luego de realizar las consultas automáticas e identificar la información a recolectar generará un archivo .xlsx que reunira los datos relacionados al proyecto consultado usando su CUI. 
<br>
<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Construido con

<a href="https://pandas.pydata.org/docs/#">
  <img src="https://pandas.pydata.org/static/img/pandas_white.svg" height=55> 
</a>


<div style="background-color: white; width: 190px; height: 35px;">
  <a href="https://openpyxl.readthedocs.io/en/stable/">
    <img src="https://openpyxl.readthedocs.io/en/stable/_static/logo.png" alt="Logo de OpenPyXL">
  </a>
</div>
 
<p style="font-family: Times, sans-serif; font-size: 24px; color: white;"><a href="https://github.com/tebelorg/RPA-Python">RPA-Python </a></p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Empezando

Para usar el paquete **SiSedeInversiones**, es necesario tener en cuenta lo siguiente:

### Pre-requisitos

El paquete fue desarrollado para python v3.11 principalmente. Aunque se hizo algunas pruebas con las versiones v3.10.

### Instalación

En la consola:

   ```cmd
   (.venv) pip install SiSedeInversiones
   ```

Al ejecutar este comando, instalamos el paquete SiSedeInversiones. 

### Atributos para el uso del paquete
Los atributos que recibe el paquete son los siguientes:

- *file_read*: Es el path de la dirección donde esta ubicado el archivo que contiene los CUI's, el paquete recibe archivos en formato .csv y no otros.
- *num_range*: Inidcamos el rango de registros que se trabajaran, ya sean desde el registro `5_10`, `2_20`... Este rango se pone a criterio del que lo use.
- *path_export*: Es la dirección de la carpeta donde se guardara el archivo que contiene toda la información que se scrapeo.
- *file_type*: Aqui indicamos el tipo de archivo que se generará al exportar la información. **De momento se tiene habilitado para .xlsx**
- *year*: En este atributo indicamos el año de los registros que se trabajaran. Ponerlo en formato string. 

### Archivo del atributo *file_read*
El paquete recibe un archivo .csv en el atributo *file_read*, este archivo debe tener dentro una columna que se llame 'cui' que contenga los Códigos Únicos de Inversion de los proyectos que quiere extraer la información que se comparte en el Sistema de Seguimiento de Inversiones.

| cui        | ...   | ...   |
|------------|-------|-------|
| 2055893    | ...   | ...   |
| 2055895    | ...   | ...   |
| 2107767    | ...   | ...   |
| 2112478    | ...   | ...   |
| 2149746    | ...   | ...   |
| ...            

**Nota:** Es necesario que dentro del archivo .csv la columna que tenga la lista de los CUI's sea llamada "cui" en minuscula. El paquete esta diseñado para ubicar dicha columna de un archivo .csv.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Uso

Para el uso del paquete **SiSedeInversiones** debemos seguir los siguiente pasos.
<br>
<br>
Para Visual Studio Code (VSC) seguimos los siguientes pases:

- Importamos el paquete.

```python
[\example.py]

from sisedeinversiones.main import SSI
```

- Luego creamos los siguientes atributos.

```python
[\example.py]

file_read = "/ruta/a/su/directorio/[nombre_archivo].csv"
path_export = "/ruta/a/su/directorio/de/destino"
num_range = "[número-inicio]_[número-final]"
file_type = ".xlsx"
year = "[año]"
```

- Instanciamos el objeto `SSI`
```python
[\example.py]

scraper = SSI(file_read, num_range, path_export, file_type, year)
```

**Importante**
<br>
Debemos mantener el orden de los atributos que se usan para instanciar la clase `SSI`. 

- Luego de instanciarlo en una clase `scraper`, podemos usar los métodos de la clase SSI.

_El metodo main_ssi() se dedica a la extracción de la información que se encuentra en el portal principal del Sistema de Seguimiento de Inversiones (https://ofi5.mef.gob.pe/ssi/ssi/Index)_
```python
[\example.py]

scraper.main_ssi()
```

![image](images/usos/ssi.png)

_Con el metodo format_eight() extraemos información del "Formato N°08-A Registros en la Fase de Ejecución"_
```python
[\example.py]

scraper.format_eight()
```

![image](images/usos/form8.jpg)

_El metodo list_ejecución() se dedica a descargar información de la página "Lista de ejecución simple pública"_

```python
[\example.py]

scraper.list_ejecucion()
```
![image](images/usos/listaEjecucionSimple.jpg)


- Por lo tanto, el código completo para ejecutar el paquete es el siguiente:

```python
[\example.py]

# Importamos la libreria
from sisedeinversiones.main import SSI

# Creamos los atribuitos
file_read = "/ruta/a/su/directorio/[nombre_archivo].csv"
path_export = "/ruta/a/su/directorio/de/destino"
num_range = "[número-inicio]_[número-final]"
file_type = ".xlsx"
year = "[año]"

# Instanciamos la clase SSI
scraper = SSI(file_read, num_range, path_export, file_type, year)

# Llamamos al metodo main_ssi()
scraper.main_ssi()

# Llamamos al método format_eight()
scraper.format_eight()

# Llamamos al método list_ejecucion()
scraper.list_ejecucion()
```

- Ejecutamos el archivo en la consola

```cmd
(.venv) python example.py
```

- Se activa una terminal que controla el paquete `rpa` que controla un navegador. Alli identificará la información que se estará almacenando en una lista. Cuando se activa este proceso se debe dejar este navegador sin usarlo. 

**Importante:** Si durante el proceso de extracción, el navegador se interrumpe por acción del que maneja, por falta de información u otra razón. 
<br>
En ese caso, se debe dar click a la consola que controla el navegador y alli se debe presionar los siguientes teclados "crtl+C" dos veces y se cerrara esa consola. Luego recien se debe cerrar el navegador que estaba controlando.

_Para más ejemplos, por favor revise la [Documentación](https://jelsinpalomino.github.io/SiSedeInversiones/)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contribuyendo

Las contribuciones son lo que hace que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. Cualquier contribución que hagas será **muy apreciada**.

Si tienes alguna sugerencia que pueda mejorar esto, haz un fork del repositorio y crea una solicitud de incorporación de cambios. También puedes abrir un problema con la etiqueta "mejora".
¡No olvides darle una estrella al proyecto! ¡Gracias de nuevo!

1. Fork del proyecto
2. Crea tu Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push tu Branch a la rama main (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request (PR)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ### Principales colaboradores:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a> -->



<!-- LICENSE -->
## Licencia

Este repositorio esta autorizado bajo la licencia MIT. Ver <a href="./LICENSE">LICENCIA</a> para mas detalles.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contacto

Jelsin Palomino - [@facebook](https://www.facebook.com/jelsinstalin.palominohuaytapuma.1) - jstpalomino@hotmail.com

Enlace del proyecto: [https://github.com/JelsinPalomino/SiSedeInversiones](https://github.com/JelsinPalomino/SiSedeInversiones)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[downloads-PyPi-shield]: https://img.shields.io/pypi/dm/sisedeinversiones
[downloads-PyPi-url]: https://pypistats.org/packages/sisedeinversiones
[contributors-shield]: https://img.shields.io/github/contributors/JelsinPalomino/SiSedeInversiones
[contributors-url]: https://github.com/JelsinPalomino/SiSedeInversiones/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JelsinPalomino/SiSedeInversiones
[forks-url]: https://github.com/JelsinPalomino/SiSedeInversiones/network/members
[stars-shield]: https://img.shields.io/github/stars/JelsinPalomino/SiSedeInversiones
[stars-url]: https://github.com/JelsinPalomino/SiSedeInversiones/stargazers
[issues-shield]: https://img.shields.io/github/issues/JelsinPalomino/SiSedeInversiones
[issues-url]: https://github.com/JelsinPalomino/SiSedeInversiones/issues
[license-shield]: https://img.shields.io/badge/License-MIT-blue
[license-url]: https://github.com/JelsinPalomino/SiSedeInversiones/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/LINKEDIN-gray
[linkedin-url]: https://www.linkedin.com/in/jstpalomino/
[product-screenshot]: images/screenshot.png
[Build-sphinx-docs-shield]:https://github.com/JelsinPalomino/SiSedeInversiones/actions/workflows/sphinx-docs.yaml/badge.svg
[Build-sphinx-docs-url]:https://github.com/JelsinPalomino/SiSedeInversiones/actions/workflows/sphinx-docs.yaml
[Test-Linters-Publish-shield]:https://github.com/JelsinPalomino/SiSedeInversiones/actions/workflows/qualityCodePublish.yaml/badge.svg
[Test-Linters-Publish-url]:https://github.com/JelsinPalomino/SiSedeInversiones/actions/workflows/qualityCodePublish.yaml
