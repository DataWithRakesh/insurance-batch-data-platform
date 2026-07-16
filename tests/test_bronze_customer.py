from src.helpers.sql_helper import get_latest_pipeline_status
from src.utils.logger import logger

def test_customer_bronze_pipeline_success():
    logger.info("Executing BR001 - Customer Bronze Pipeline status")
    pipeline = get_latest_pipeline_status("pl_customer_landing_to_bronze")
    assert pipeline is not None, "No pipeline run found for pl_customer_landing_to_bronze"
    assert pipeline.status == "SUCESS", f"Expected status 'SUCCESS', but got '{pipeline.status}'"
    logger.info("BR001 Passed")
