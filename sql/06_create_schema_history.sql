
CREATE TABLE schema_history (
    source_name      VARCHAR(100),
    schema_version   INT,
    schema_json      NVARCHAR(MAX),
    detected_on      DATETIME2,
    change_type      VARCHAR(20),
    status           VARCHAR(20)
);
