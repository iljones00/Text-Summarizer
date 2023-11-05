from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage 01"
try:
    logger.info(f"Started {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

