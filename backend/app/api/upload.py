from fastapi import APIRouter, UploadFile, File
# uploadFile contains filename,size,content,metadata
from app.ingestion.ingest_service import IngestionService
import shutil
from pathlib import Path # to make more readable path

router = APIRouter()


UPLOAD_DIR = Path("app/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True) #if above path not exists then make it 


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    ingestor = IngestionService()
    
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer) # this copies object on Disk
    
    result = ingestor.ingest(file_path)


    return {
        "status": "Document Indexed Successfully",
        **result
    }

