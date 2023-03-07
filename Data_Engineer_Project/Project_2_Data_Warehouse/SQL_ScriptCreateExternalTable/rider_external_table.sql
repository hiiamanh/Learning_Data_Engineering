IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'anhbn15_anhbn15_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [anhbn15_anhbn15_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://anhbn15@anhbn15.dfs.core.windows.net', 
		TYPE = HADOOP 
	)
GO

CREATE EXTERNAL TABLE dbo.staging_rider (
	[rider_id] bigint,
	[address] nvarchar(4000),
	[first_name] nvarchar(4000),
	[last_name] nvarchar(4000),
	[birthday] nvarchar(4000),
	[start_date] nvarchar(4000),
	[end_date] nvarchar(4000),
	[is_member] bit
	)
	WITH (
	LOCATION = 'publicrider.csv',
	DATA_SOURCE = [anhbn15_anhbn15_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM dbo.staging_rider
GO