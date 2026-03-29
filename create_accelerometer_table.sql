CREATE EXTERNAL TABLE accelerometer_landing (
    user STRING,
    timestamp BIGINT,
    x FLOAT,
    y FLOAT,
    z FLOAT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('ignore.malformed.json' = 'TRUE')
LOCATION 's3://casey-schrader2/accelerometer/landing/'
TBLPROPERTIES ('classification' = 'json');