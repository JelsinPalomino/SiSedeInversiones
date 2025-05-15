from sisedeinversiones.main import SSI

file_read = "E:\..\..\..\SiSedeInversiones\examples\CUI_2019_dep7.csv"
path_export = "E:\..\..\..\SiSedeInversiones\examples"
num_range = "5_10"
file_type = ".xlsx"
year = "2019"

scraper = SSI(file_read, num_range, path_export, file_type, year)
scraper.format_eight()
# scraper.list_ejecucion()
# scraper.main_ssi()


