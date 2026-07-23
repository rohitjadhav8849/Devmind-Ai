from app.ingestion.ingest_service import IngestionService

ingestor = IngestionService()

ingestor.ingest(
  "app/data/uploads/demo.pdf"
)