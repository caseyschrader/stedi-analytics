CREATE EXTERNAL TABLE customer_landing (
    customerName STRING,
    email STRING,
    phone STRING,
    birthDay STRING,
    serialNumber STRING,
    registrationDate BIGINT,
    lastUpdateDate BIGINT,
    shareWithResearchAsOfDate BIGINT,
    shareWithPublicAsOfDate BIGINT,
    shareWithFriendsAsOfDate BIGINT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('ignore.malformed.json' = 'TRUE')
LOCATION 's3://casey-schrader2/customer/landing/'
TBLPROPERTIES ('classification' = 'json');