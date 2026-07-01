
CREATE TABLE pipeline_run (
    run_id          VARCHAR(100) PRIMARY KEY,
    pipeline_name   VARCHAR(100),
    batch_date      DATE,
    status          VARCHAR(20),
    start_time      DATETIME2,
    end_time        DATETIME2,
    triggered_by    VARCHAR(50),
    error_message   VARCHAR(MAX)
);
