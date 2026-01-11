

DELETE FROM Customers;
DELETE Customers WHERE Id = 10;  
DELETE TOP (10) FROM dbo.Customers;
DELETE TOP (5) PERCENT FROM dbo.Customers WHERE City = 'Chicago';