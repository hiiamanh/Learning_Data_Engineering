IF OBJECT_ID('dbo.dimStation') IS NOT NULL
    DROP TABLE dbo.dimStation;
CREATE TABLE dbo.dimStation
    WITH
    ( 
        DISTRIBUTION = REPLICATE, 
        CLUSTERED COLUMNSTORE INDEX
    )
    AS
        SELECT
            [station_id],
            [name],
            [latiude],
            [longitude]
        FROM
            staging_station;

SELECT TOP 10 * FROM dimStation;

