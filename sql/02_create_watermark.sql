
CREATE TABLE watermark (
    source_name          VARCHAR(100) PRIMARY KEY,
    watermark_column     VARCHAR(100),
    last_watermark_value DATETIME2,
    last_batch_date      DATE,
    updated_ts           DATETIME2
);
