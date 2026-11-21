# Task 1
SELECT customerName, phone, city, country 
FROM customers 
LIMIT 10;

# Task 2
SELECT * 
FROM customers 
WHERE postalCode > 1370 AND salesRepEmployeeNumber > 150 
LIMIT 10;

# Task 3
SELECT * 
FROM customers 
WHERE customerName LIKE '%Mini%' 
LIMIT 10;

# Task 4
SELECT * 
FROM customers 
WHERE state = 'CA' OR state = 'NY' 
LIMIT 10;

# Task 5
SELECT * 
FROM customers 
WHERE creditLimit > 10000 
LIMIT 10;
