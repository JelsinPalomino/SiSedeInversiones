# from .sisedeinversiones.format_eight import Scraping
# import sisedeinversiones as ssi
# from sisedeinversiones.form_eight import Scraping
from sisedeinversiones.form_eight.eight import ScrapingEight

# file_read = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/scrapingFunctions/SiSedeInversiones/CUI_2019_dep7.csv"
file_read = "CUI_2019_dep7.csv"
path_export = "E:/otrosTrabajosSTATA-practicas/proyectStataPythonToGitHub/pruebas"
num_range = "5_10"
file_type = ".xlsx"
year = "2019"

# scraper = ssi.format_eight.Scraping(file_read, path_export, num_range, file_type, year)

scraper = ScrapingEight(file_read, num_range, path_export, file_type, year)
# scraper.shows_params()
scraper.download_data()
