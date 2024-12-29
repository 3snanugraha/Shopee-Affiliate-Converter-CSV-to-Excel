import os
import csv
import pandas as pd

class DataConverter:
    def __init__(self):
        self.base_folder = "basedata"
        self.output_folder = "outputs"
        self.output_excel = "outputs/datakomisi.xlsx"  # Changed to xlsx
        self.results = []
        self.current_number = 1

    def setup_folders(self):
        os.makedirs(self.output_folder, exist_ok=True)

    def read_csv_files(self):
        csv_files = []
        for file in os.listdir(self.base_folder):
            if file.endswith('.csv'):
                csv_files.append(os.path.join(self.base_folder, file))
        return csv_files

    def process_csv_data(self):
        csv_files = self.read_csv_files()
        
        for csv_file in csv_files:
            with open(csv_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    result = {
                        "Number": self.current_number,
                        "ID Produk": row.get('ID Produk', ''),
                        "Nama Produk": row.get('Nama Produk', ''),
                        "Harga": row.get('Harga', ''),
                        "Penjualan": row.get('Penjualan', ''),
                        "Nama Toko": row.get('Nama Toko', ''),
                        "Komisi hingga": row.get('Komisi hingga', ''),
                        "Komisi": row.get('Komisi', ''),
                        "Link Produk": row.get('Link Produk', ''),
                        "Link Komisi Ekstra": row.get('Link Komisi Ekstra', '')
                    }
                    self.results.append(result)
                    print(f"Processed item {self.current_number}")
                    self.current_number += 1

    def save_results(self):
        df = pd.DataFrame(self.results)
        df.to_excel(self.output_excel, index=False)
        print(f"Results saved to {self.output_excel}")

    def run(self):
        print("Starting CSV to Excel conversion...")
        self.setup_folders()
        self.process_csv_data()
        self.save_results()
        print("Conversion completed!")

if __name__ == "__main__":
    converter = DataConverter()
    converter.run()
