from fastapi import APIRouter, UploadFile, File
# uploadFile contains filename,size,content,metadata
from app.services.document_processor import DocumentProcessor
from app.services.chunker import TextChunker
import shutil
from pathlib import Path # to make more readable path

router = APIRouter()
processor = DocumentProcessor() 
chunker = TextChunker()



UPLOAD_DIR = Path("app/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True) #if above path not exists then make it 


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer) # this copies object on Disk
    
    text = processor.extract_text(file_path)
    chunks = chunker.chunk(text)


    return {
        "filename": file.filename,
        "status": "uploaded successfully",
        "characters" : len(text),
        "preview": text[:500],
        "first_chunk" : chunks[0]
    }

