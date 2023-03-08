IF OBJECT_ID('dbo.dimRider') IS NOT NULL
    DROP TABLE dbo.dimRider;
CREATE TABLE dbo.dimRider
(
    rider_id BIGINT NOT NULL PRIMARY KEY NONCLUSTERED NOT ENFORCED,
    first_name NVARCHAR(4000),
    last_name NVARCHAR(4000),
    address NVARCHAR(4000),
    birthday DATETIME2,
    account_start_date DATETIME2,
    account_end_date DATETIME2,
    is_member BIT
)

INSERT INTO dbo.dimRider
SELECT
    [rider_id] as rider_id,
    [first_name] as first_name,
    [last_name] as last_name,
    [address] as address,
    TRY_CONVERT(DATETIME2,left(birthday,19)) as birthday,
    TRY_CONVERT(DATETIME2,left(start_date,19)) as account_start_date,
    TRY_CONVERT(DATETIME2,left(end_date,19)) as account_end_date,
    [is_member] as is_member
FROM dbo.staging_rider;

SELECT TOP 10 * FROM dbo.dimRider;

