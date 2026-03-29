CREATE EXTERNAL TABLE step_trainer_landing (
    sensorReadingTime BIGINT,
    serialNumber STRING,
    distanceFromObject BIGINT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('ignore.malformed.json' = 'TRUE')
LOCATION 's3://casey-schrader2/step_trainer/landing/'
TBLPROPERTIES ('classification' = 'json');