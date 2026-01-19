DELETE FROM dbo.TableA;

DELETE dbo.TableA;

DELETE TOP (5) FROM dbo.TableA;

DELETE FROM dbo.TableA
OUTPUT deleted.id;

DELETE FROM dbo.TableA
WHERE col1 = 10;

DELETE a
FROM dbo.TableA a
JOIN dbo.TableB b ON a.id = b.id
WHERE b.flag = 1;

DELETE a
FROM dbo.TableA AS a;

DELETE FROM @myTable;

WITH cte AS (
    SELECT id FROM dbo.TableA WHERE flag = 1
)
DELETE FROM dbo.TableA
WHERE id IN (SELECT id FROM cte);

DELETE FROM dbo.TableA
OUTPUT deleted.id, deleted.col1
WHERE col1 > 100;

DELETE dbo.TableA
WHERE col2 IS NULL;

WITH cte AS (
    SELECT id FROM dbo.TableB
)
DELETE TOP (3) a
OUTPUT deleted.id
FROM dbo.TableA a
JOIN cte ON a.id = cte.id
WHERE a.status = 'X';

DELETE FROM Customers;
DELETE Customers WHERE Id = 10;
DELETE TOP (10) FROM dbo.Customers;
DELETE TOP (5) PERCENT FROM dbo.Customers WHERE City = 'Chicago';
DELETE spqh FROM Sales.SalesPersonQuotaHistory AS spqh INNER JOIN Sales.SalesPerson AS sp ON spqh.BusinessEntityID = sp.BusinessEntityID WHERE sp.SalesYTD > 2500000.00;

DELETE FROM Sales.SalesPersonQuotaHistory;

DELETE Sales.SalesPersonQuotaHistory;

DELETE Production.ProductCostHistory
WHERE StandardCost > MaxStandardCost;

DELETE Production.ProductCostHistory
WHERE StandardCost BETWEEN MinCost AND MaxCost
  AND EndDate IS NULL;

DELETE Production.ProductCostHistory
WHERE ProductCode IN (CodeA, CodeB, CodeC);

DELETE Production.ProductCostHistory
WHERE EndDate IS NOT NULL;

DELETE FROM HumanResources.EmployeePayHistory
WHERE CURRENT OF complex_cursor;

DELETE TOP (10)
FROM Purchasing.PurchaseOrderDetail
WHERE DueDate < OldestDueDate;


DELETE TOP (5) PERCENT
FROM Purchasing.PurchaseOrderDetail
WHERE DueDate < OldestDueDate;

DELETE FROM Sales.SalesPersonQuotaHistory
FROM Sales.SalesPersonQuotaHistory AS spqh
INNER JOIN Sales.SalesPerson AS sp
  ON spqh.BusinessEntityID = sp.BusinessEntityID
WHERE sp.SalesYTD > TargetSales;

DELETE FROM Sales.SalesPersonQuotaHistory
FROM Sales.SalesPersonQuotaHistory AS spqh
JOIN Sales.SalesPerson AS sp
  ON spqh.BusinessEntityID = sp.BusinessEntityID
WHERE sp.SalesYTD > TargetSales;

DELETE FROM dbo.BigTable
FROM dbo.BigTable AS bt
INNER JOIN dbo.OtherTable AS ot
  ON bt.Id = ot.Id
WHERE (bt.Flag IS NULL OR bt.Flag IS NOT NULL)
  AND bt.ColA IN (Val1, Val2)
  AND bt.ColB BETWEEN LowerBound AND UpperBound;
DELETE Sales.ShoppingCartItem
OUTPUT DELETED.*
WHERE ShoppingCartID = 20621;

