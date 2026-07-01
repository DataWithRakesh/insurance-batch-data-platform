
CREATE TABLE metadata (
    source_name          VARCHAR(100) PRIMARY KEY,
    source_path          VARCHAR(500),
    bronze_table         VARCHAR(100),
    silver_table         VARCHAR(100),
    gold_table           VARCHAR(100),
    file_format          VARCHAR(20),
    business_key         VARCHAR(100),
    watermark_column     VARCHAR(100),
    is_active            CHAR(1)
);
