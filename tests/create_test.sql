CREATE TABLE Customers
(
    CustomerID INT NOT NULL,
    Name NVARCHAR(100) NULL
);

CREATE TABLE Sales.Orders
(
    OrderID INT NOT NULL,
    CustomerID INT NOT NULL,
    OrderDate DATETIME2 NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Orders PRIMARY KEY (OrderID),
    CONSTRAINT FK_Orders_Customers FOREIGN KEY (CustomerID)
        REFERENCES Customers (CustomerID),
    CONSTRAINT CK_Orders_TotalAmount CHECK (TotalAmount > 0)
);


CREATE INDEX IX_Customers_Name
ON Customers (Name);

CREATE INDEX IX_Customers_Name_Email
ON dbo.Customers (Name ASC, Email DESC);

CREATE CLUSTERED INDEX IX_Orders_OrderDate
ON SalesDB.dbo.Orders (OrderDate);

CREATE UNIQUE INDEX IX_Customers_Email_Unique
ON dbo.Customers (Email ASC, Country DESC);

CREATE NONCLUSTERED INDEX IX_Orders_CustomerId
ON dbo.Orders (CustomerID)
INCLUDE (OrderDate, TotalAmount);

CREATE NONCLUSTERED INDEX IX_Orders_OpenOrders
ON dbo.Orders (Status)
WHERE Status = 'Open';

CREATE NONCLUSTERED INDEX IX_Orders_TotalAmount
ON dbo.Orders (TotalAmount DESC)
WITH (
    PAD_INDEX = ON,
    FILLFACTOR = 80,
    IGNORE_DUP_KEY = OFF,
    ALLOW_ROW_LOCKS = ON,
    ALLOW_PAGE_LOCKS = OFF
);
