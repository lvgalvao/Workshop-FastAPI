from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import csv
import io

app = FastAPI()

@app.get("/download-csv/")
def download_csv():
    data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
    stream = io.StringIO()
    writer = csv.writer(stream)
    writer.writerows(data)
    stream.seek(0)
    return StreamingResponse(iter([stream.read()]), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=report.csv"})
