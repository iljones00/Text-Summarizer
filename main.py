from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
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

STAGE_NAME = "Data Validation Stage 02"
try:
    logger.info(f"Started {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage 03"
try:
    logger.info(f"Started {STAGE_NAME}")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e