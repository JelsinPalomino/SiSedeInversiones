"""
* Class read_utils
==================
"""
import pandas as pd

class ReadsFiles:
    def __init__(self, file_read, num_range):
        self.file_read = file_read
        self.num_range = num_range

    def read_file_csv(self):
        start_range, end_range = self.num_range.split("_")
        cui0 = pd.read_csv(self.file_read, encoding="latin-1")
        cui1 = cui0["cui"][int(start_range):int(end_range)]
        list_cui = list(map(str, cui1.values.tolist()))
        print(f"El total de CUIs a scrapear es: {len(list_cui)}")
        return list_cui
    
    def read_file_xlsx(self):
        start_range, end_range = self.num_range.split("_")
        cui0 = pd.read_excel(self.file_read, encoding="latin-1")
        cui1 = cui0["cui"][int(start_range):int(end_range)]
        list_cui = list(map(str, cui1.values.tolist()))
        print(f"El total de CUIs a scrapear es: {len(list_cui)}")
        return list_cui