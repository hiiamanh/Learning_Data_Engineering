IF OBJECT_ID('dbo.dimDate') IS NOT NULL
    DROP TABLE dbo.dimDate;
CREATE TABLE dbo.dimDate
(
    date_id uniqueidentifier NOT NULL PRIMARY KEY NONCLUSTERED NOT ENFORCED,
    date DATETIME2,
    year int,
    quarter int,
    month int,
    day int,
    week int
)

DECLARE @Started_date DATETIME2
DECLARE @Ended_date DATETIME2

SET @Started_date = (SELECT MIN(TRY_CONVERT(DATETIME2,left(started_at,19))) FROM dbo.staging_trip)
SET @Ended_date = (SELECT MAX(TRY_CONVERT(DATETIME2,left(ended_at,19))) FROM dbo.staging_trip)

WHILE @Started_date <= @Ended_date
    BEGIN
        INSERT INTO dbo.dimDate
            SELECT 
                NEWID() as date_id,
                @Started_date as date,
                DATEPART(YEAR,@Started_date) as year,
                DATEPART(QUARTER,@Started_date) as quarter,
                DATEPART(MONTH,@Started_date) as month,
                DATEPART(DAY,@Started_date) as day,
                DATEPART(WEEK,@Started_date) as week
            
            SET @Started_date = DATEADD(day,1,@Started_date)
    END;

SELECT TOP 10 * FROM dbo.dimDate