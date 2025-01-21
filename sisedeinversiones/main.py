from .form_eight.eight import ScrapingEight
from .lista_ejecucion.lista_ejecucion_simple import ScrapingListaEjecucion
from .ssi.main_ssi import ScrapingMainSSI

class SSI(ScrapingEight, ScrapingListaEjecucion, ScrapingMainSSI):
    def __init__(self, file_read, num_range, path_export, file_type, year):
        ScrapingEight.__init__(self, file_read, num_range, path_export, file_type, year)
        ScrapingListaEjecucion.__init__(self, file_read, num_range, path_export, file_type, year)
        ScrapingMainSSI.__init__(self, file_read, num_range, path_export, file_type, year)

    def format_eight (self):
        return ScrapingEight(
            self.file_read, 
            self.num_range, 
            self.path_export, 
            self.file_type, 
            self.year
            ).download_data()
    
    def list_ejecucion(self):
        return ScrapingListaEjecucion(
            self.file_read, 
            self.num_range, 
            self.path_export, 
            self.file_type, 
            self.year
            ).download_data()

    def main_ssi(self):
        return ScrapingMainSSI(
            self.file_read, 
            self.num_range, 
            self.path_export, 
            self.file_type, 
            self.year
            ).download_data()
    