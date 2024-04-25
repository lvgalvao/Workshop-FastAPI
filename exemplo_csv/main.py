from fastapi import FastAPI
import csv
from io import StringIO

app = FastAPI()

@app.get("/download-csv/")
def download_csv():
    # Dados que queremos enviar em formato CSV
    data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
    
    # Utilizar StringIO para simular um arquivo
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    
    # Retornar o conteúdo CSV como uma string simples
    return output.getvalue()
