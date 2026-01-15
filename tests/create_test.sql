
-- Multi-statement TVF مع @return_variable TABLE (...)
CREATE FUNCTION dbo.SplitInts (@list NVARCHAR(MAX))
RETURNS @Result TABLE
(
    Value INT NOT NULL
)
WITH SCHEMABINDING, EXECUTE AS OWNER
AS
BEGIN
    INSERT INTO @Result (Value)
    SELECT TRY_CONVERT(INT, value)
    FROM dbo.StringSplit(@list, ',');

    RETURN
END;
