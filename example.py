# from .sisedeinversiones.format_eight import Scraping
# import sisedeinversiones as ssi
# from sisedeinversiones.form_eight import Scraping
from sisedeinversiones.form_eight.eight import ScrapingEight
from sisedeinversiones.lista_ejecucion.lista_ejecucion_simple import ScrapingListaEjecucion
from sisedeinversiones.ssi.main_ssi import ScrapingMainSSI

# file_read = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/scrapingFunctions/SiSedeInversiones/CUI_2019_dep7.csv"
file_read = "CUI_2019_dep7.csv"
path_export = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/pruebas"
num_range = "5_10"
file_type = ".xlsx"
year = "2019"

# scraper = ssi.format_eight.Scraping(file_read, path_export, num_range, file_type, year)

# scraperEight = ScrapingEight(file_read, num_range, path_export, file_type, year)
# scraperEight.download_data()

# scraperListaEjecucion = ScrapingListaEjecucion(file_read, num_range, path_export, file_type, year)
# scraperListaEjecucion.download_data()

scraperMainSSI = ScrapingMainSSI(file_read, num_range, path_export, file_type, year)
scraperMainSSI.download_data()