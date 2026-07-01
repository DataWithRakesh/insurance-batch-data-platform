
CREATE TABLE error_log (
    run_id            VARCHAR(100),
    pipeline_name     VARCHAR(100),
    notebook_name     VARCHAR(100),
    source_name       VARCHAR(100),
    layer             VARCHAR(50),
    error_message     VARCHAR(MAX),
    error_timestamp   DATETIME2,
    batch_date        DATE
);
