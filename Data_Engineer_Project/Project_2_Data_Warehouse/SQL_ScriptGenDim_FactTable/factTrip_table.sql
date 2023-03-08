IF OBJECT_ID('dbo.factTrip') IS NOT NULL
    DROP TABLE dbo.factTrip;

CREATE TABLE dbo.factTrip
(
    trip_id NVARCHAR(4000) NOT NULL PRIMARY KEY NONCLUSTERED NOT ENFORCED,
    rider_id BIGINT,
    rider_type NVARCHAR(4000),
    rider_age INT,
    trip_duration INT,
    started_at DATETIME2,
    ended_at DATETIME2,
    start_station_id NVARCHAR(4000),
    end_station_id NVARCHAR(4000)
);

INSERT INTO dbo.factTrip
SELECT 
    st.trip_id as trip_id,
    st.member_id as rider_id,
    st.rideable_type as rider_type,
    DATEDIFF(YEAR,sr.birthday,st.started_at) as rider_age,
    DATEDIFF(MINUTE,st.started_at,st.ended_at) as trip_duration,
    st.started_at as started_at,
    st.ended_at as ended_at,
    st.start_station_id as start_station_id,
    st.end_station_id as end_station_id 
FROM dbo.staging_trip st
JOIN dbo.staging_rider sr ON sr.rider_id = st.member_id ;

SELECT TOP 10 * FROM dbo.factTrip