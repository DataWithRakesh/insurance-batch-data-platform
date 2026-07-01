
CREATE TABLE audit (
    run_id              VARCHAR(100),
    source_name         VARCHAR(100),
    layer               VARCHAR(50),
    batch_date          DATE,
    records_read        INT,
    records_written     INT,
    records_rejected    INT,
    status              VARCHAR(20),
    start_time          DATETIME2,
    end_time            DATETIME2,
    duration_seconds    INT
);
