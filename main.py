from LogisticRegression import logger
from LogisticRegression.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from LogisticRegression.pipeline.stage_02_data_validation import DataValidationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_validation = DataValidationPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e