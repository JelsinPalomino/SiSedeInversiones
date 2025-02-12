"""
1.- Sistema de Seguimiento de Inversiones (SSI)
===============================================

Es una herramienta informática de acceso público que permite el seguimiento de
las inversiones públicas e integra información de las diferentes fases del ciclo de
inversión como Programación Multianual de Inversiones, Formulación y
del Estado como Sistema Nacional de Programacion Multianual y Gestión de
Evaluación, y Ejecución. Además, está vinculado con varios sistemas informáticos
Inversiones – Invierte.pe, SEACE, InfObras y SIAF. [#]_ 

.. [#] Extraido de (S/f). Gob.pe. Recuperado el 19 de enero de 2025, de https://www.mef.gob.pe/contenidos/inv_publica/docs/Instructivo_BI/2024/Seguimiento_2_Manual_SSI.pdf.

1.1. Objetivos del SSI
----------------------

+--------+---------------------------------------------------------------------------------------------------------------------------------------------+
| N°     | Objetivos                                                                                                                                   | 
+========+=============================================================================================================================================+
| 01     | Mostrar información sistematizada de las inversiones públicas, para un adecuado seguimiento                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------+
| 02     | Optimizar el tiempo de búsqueda a través de los vinculos de acceso con los formatos de las diferentes fases del Ciclo de Inversión          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------+
| 03     | Brindar información actualizada de las inversiones con la finalidad de facilitar la elaboración de reportes de seguimiento.                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------+
| 04     | Conocer los actores que intervienen en la gestión de la Inversión Pública (UEI, UF y OPMI)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------+


1.2. Entorno del SSI
--------------------

.. image:: _static/ssi.png

1.3. Secciones del SSI
----------------------

1.3.1 Sección: Datos generales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al momento de ubicar el proyecto de inversión pública, ya sea por medio del
Código Único de Inversión (CUI) o por el nombre, se despliegan cuatro secciones:

- Institucionalidad
- Datos de la fase de Formulación y Evaluación
- Datos de la fase de Ejecución
- Registro de Obras Paralizadas

.. image:: _static/datosGenerales.PNG


1.3.2 Sección: Ejecución financiera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez ubicada el proyecto de inversión pública que se busco dentro del Sistema de 
Seguimiento de Inversión, para ingresar a esta sección se debe dar click al boton 
**Ejecución financiera**, esta acción mostrara las siguiente cuatro secciones:

- Información financiera
- Histórico de devengado de la inversión
- Histórico de devengado por específica
- Detalle por Unidad Ejecutora Presupuestal

.. image:: _static/ejecucionFinanciera.png


1.3.3 Sección: Contrataciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al momento de tener identificado el proyecto de inversión pública también
se puede dar click al boton **Contrataciones**. Lo que presentará los contratos 
asociados al proyecto que se esta consultando, los que estaran agrupados 
de la siguiente manera:

- Contratos de bienes
- Contratos de servicios
- Contratos de obras

.. image:: _static/Contrataciones.png


.. note:: 
   Solo se muestran los contratos suscritos en el marco de la **Ley de Contrataciones del Estado**, esta información se obtiene de una conexión con SEACE.

.. important:: 
   Para descargar los contratos se debe dar click en el ícono **Documento PDF**.

   
   
1.3.4 Sección: InfObras
^^^^^^^^^^^^^^^^^^^^^^^

Cuando se identificó el proyecto de inversión pública, para ingresar a esta sección
se debe dar click al boton **InfObras**, donde se presentara las siguientes subsecciones:

- Datos generales 
- Avance físico de la obra

.. image:: _static/InfObras.png


2.- Instalación de la biblioteca "SiSedeInversiones"
====================================================

2.1. Instalación por consola
----------------------------

La biblioteca *SiSedeInversiones* se puede instalar desde la consola con el siguiente comando:

.. code-block:: console

    (.venv) $ pip install SiSedeInversiones

"""

__all__ = ["main", "form_eight", "lista_ejecucion"]
