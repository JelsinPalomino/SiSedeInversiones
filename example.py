# from .sisedeinversiones.format_eight import Scraping
# import sisedeinversiones as ssi
from sisedeinversiones.format_eight import Scraping


file_read = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/scrapingFunctions/SiSedeInversiones/sisedeinversiones/format_eight/CUI_2019_dep7.csv"
path_export = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/pruebas"
num_range = "5_10"
file_type = ".xlsx"
year = "2019"

# scraper = ssi.format_eight.Scraping(file_read, path_export, num_range, file_type, year)

scraper = Scraping(file_read, path_export, num_range, file_type, year)
scraper.download_data()
