IF OBJECT_ID('dbo.factPayment') IS NOT NULL
    DROP TABLE dbo.factPayment;

CREATE TABLE dbo.factPayment
(
    payment_id BIGINT NOT NULL PRIMARY KEY NONCLUSTERED NOT ENFORCED,
    date DATETIME2,
    rider_id BIGINT,
    amount FLOAT
)

INSERT INTO dbo.factPayment
SELECT
    sp.payment_id as payment_id,
    sp.date as date,
    sp.account_number as rider_id,
    sp.amount as amount
FROM dbo.staging_payment sp

SELECT TOP 10 * FROM dbo.factPayment