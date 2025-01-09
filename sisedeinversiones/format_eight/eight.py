import pandas as pd
import rpa as r
import time
import os

cui = pd.read_csv("E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/scrapingFunctions/sise-de-inversiones/sisedeinversiones/format_eight/CUI_2019_dep7.csv", encoding='latin-1') 
cui0 = cui.rename(columns = {'PRODUCTO_PROYECTO': 'cui', '"PRODUCTO_PROYECTO"': 'cantidad'})

cui1 = cui0['cui']
cui2 = cui1[1:10]

rango = "1_10"
path_export = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/pruebas/ssi_formato8_2019_"
filetype = ".xlsx"

lista_cui0 = cui2.values.tolist()
lista_cui = list(map(str, lista_cui0))
print(lista_cui)

r.init()
# r.init(turbo_mode=True)


# -----------------------------------------------------------------------------------------
# ----------------------CREAMOS LAS LISTAS PARA ALMACENAR LA INFORMACIÓN-------------------
# -----------------------------------------------------------------------------------------

# Responsabilidad funcional del proyecto de inversion
ssi_cui                             = []
ssi_pip                             = []
ssi_funcion                         = []
ssi_divfuncional                    = []
ssi_grupfuncional                   = []
ssi_sectorresponsable               = []
# Articulacion con el programa multianual de inversiones (PMI)
ssi_brecha                          = []
ssi_brecha_indicador                = []
ssi_brecha_um                       = []
ssi_brecha_espaciogeografico        = []
ssi_brecha_contribucioncierre       = []
# Institucionalidad
ssi_opmi                            = []
ssi_uf                              = []
ssi_uei                             = []
ssi_uep                             = []
# Localizacion de la inversion publica
ssi_gps                             = []
ssi_departamento                    = []
ssi_provincia                       = []
ssi_distrito                        = []
ssi_centro_poblado                  = []

# -------------------------------------------------------------------------
#----------------------SCRAPEO DE LA INFORMACIÓN POR CUI-------------------
# -------------------------------------------------------------------------

for i in range(len(lista_cui)):
    r.url(f'https://ofi5.mef.gob.pe/invierte/ejecucion/verFichaEjecucion/{lista_cui[i]}')
    time.sleep(3)

    element_exist = r.present('//*[@id="divVistaPreliminar"]/table[1]/tbody/tr[1]/td[1]')
    print(i, element_exist)
    if element_exist==True:
        time.sleep(2)

        #Identificamos la infor que se va extraer
        cui                              = r.read('//*[@id="divVistaPreliminar"]/table[1]/tbody/tr[1]/td[2]/div')
        pip                              = r.read('//*[@id="divVistaPreliminar"]/table[1]/tbody/tr[2]/td[2]/div')
        funcion                          = r.read('//*[@id="divVistaPreliminar"]/table[2]/tbody/tr[1]/td[3]')
        divfuncional                     = r.read('//*[@id="divVistaPreliminar"]/table[2]/tbody/tr[2]/td[3]')
        grupfuncional                    = r.read('//*[@id="divVistaPreliminar"]/table[2]/tbody/tr[3]/td[3]')
        sectorresponsable                = r.read('//*[@id="divVistaPreliminar"]/table[2]/tbody/tr[4]/td[3]')

        brecha                           = r.read('//*[@id="divVistaPreliminar"]/table[3]/tbody/tr/td[1]')
        brecha_indicador                 = r.read('//*[@id="divVistaPreliminar"]/table[3]/tbody/tr/td[2]')
        brecha_um                        = r.read('//*[@id="divVistaPreliminar"]/table[3]/tbody/tr/td[3]')
        brecha_espaciogeografico         = r.read('//*[@id="divVistaPreliminar"]/table[3]/tbody/tr/td[4]')
        brecha_contribucioncierre        = r.read('//*[@id="divVistaPreliminar"]/table[3]/tbody/tr/td[5]')

        opmi                             = r.read('//*[@id="divVistaPreliminar"]/table[4]/tbody/tr[1]/td[3]')
        uf                               = r.read('//*[@id="divVistaPreliminar"]/table[4]/tbody/tr[2]/td[3]')
        uei                              = r.read('//*[@id="divVistaPreliminar"]/table[4]/tbody/tr[3]/td[3]')
        uep                              = r.read('//*[@id="divVistaPreliminar"]/table[4]/tbody/tr[4]/td[3]')

        element_exist1 = r.present('//*[@id="divVistaPreliminar"]/table[6]/tbody/tr/td[1]')
        if element_exist1 ==True:
            gps                              = r.read('//*[@id="divVistaPreliminar"]/table[5]/tbody/tr/td[1]')
            departamento                     = r.read('//*[@id="divVistaPreliminar"]/table[5]/tbody/tr/td[2]')
            provincia                        = r.read('//*[@id="divVistaPreliminar"]/table[5]/tbody/tr/td[3]')
            distrito                         = r.read('//*[@id="divVistaPreliminar"]/table[5]/tbody/tr/td[4]')
            centro_poblado                   = r.read('//*[@id="divVistaPreliminar"]/table[5]/tbody/tr/td[5]')
        
        else:
            gps                              = 0
            departamento                     = 0
            provincia                        = 0
            distrito                         = 0
            centro_poblado                   = 0

        ssi_cui.append(cui)
        ssi_pip.append(pip)
        ssi_funcion.append(funcion)
        ssi_divfuncional.append(divfuncional)
        ssi_grupfuncional.append(grupfuncional)
        ssi_sectorresponsable.append(sectorresponsable)

        ssi_brecha.append(brecha)
        ssi_brecha_indicador.append(brecha_indicador)
        ssi_brecha_um.append(brecha_um)
        ssi_brecha_espaciogeografico.append(brecha_espaciogeografico)
        ssi_brecha_contribucioncierre.append(brecha_contribucioncierre)

        ssi_opmi.append(opmi)
        ssi_uf.append(uf)
        ssi_uei.append(uei)
        ssi_uep.append(uep)

        ssi_gps.append(gps)
        ssi_departamento.append(departamento)
        ssi_provincia.append(provincia)
        ssi_distrito.append(distrito)
        ssi_centro_poblado.append(centro_poblado)
        
        

    elif element_exist == False:
    
        continue
    
r.close()

time.sleep(2)

# Creamos el dataframe 
ssi_formato8_2019 = pd.DataFrame({
    "cui"                      : ssi_cui,
    "nombre_pip"               : ssi_pip,
    "funcion"                  : ssi_funcion,
    "division_funcional"       : ssi_divfuncional,
    "grupo_funcional"          : ssi_grupfuncional,
    "sector_responsable"       : ssi_sectorresponsable,
    
    "brecha_identificada"      : ssi_brecha,
    "brecha_indicador"         : ssi_brecha_indicador,
    "brecha_unidad"            : ssi_brecha_um,
    "espacio_geografico"       : ssi_brecha_espaciogeografico,
    "cierre_brechas"           : ssi_brecha_contribucioncierre,

    "opmi"                     : ssi_opmi,
    "uf"                       : ssi_uf,
    "uei"                      : ssi_uei,
    "uep"                      : ssi_uep,
    
    "gps"                      : ssi_gps,
    "departamento"             : ssi_departamento,
    "provincia"                : ssi_provincia,
    "distrito"                 : ssi_distrito,
    "centro_poblado"           : ssi_centro_poblado
})

ssi_formato8_2019.to_excel(path_export+rango+filetype, index = False, header=True)