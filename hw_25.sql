-- დავალება 1
SELECT customerName, phone, city, country 
FROM customers 
LIMIT 10;

-- დავალება 2
SELECT * 
FROM customers 
WHERE postalCode > 1370 AND salesRepEmployeeNumber > 150 
LIMIT 10;

-- დავალება 3
SELECT * 
FROM customers 
WHERE customerName LIKE '%Mini%' 
LIMIT 10;

-- დავალება 4
SELECT * 
FROM customers 
WHERE state = 'CA' OR state = 'NY' 
LIMIT 10;

-- დავალება 5
SELECT * 
FROM customers 
WHERE creditLimit > 10000 
LIMIT 10;