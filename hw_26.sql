-- 1. Authors ცხრილის შექმნა (პირველადი გასაღებით)
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

-- 2. Books ცხრილის შექმნა (მეორადი გასაღებით AuthorID)
CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100),
    Price DECIMAL(10, 2),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
);

-- 3. ჩანაწერების დამატება (მინიმუმ 5 ჩანაწერი თითო ცხრილში)
INSERT INTO Authors (FirstName, LastName) VALUES
('J.K.', 'Rowling'),
('George', 'Orwell'),
('Ana', 'Kalandadze'),
('Luka', 'Beridze'),
('Saba', 'Gelashvili');

INSERT INTO Books (Title, Price, AuthorID) VALUES
('Harry Potter', 35.00, 1),
('1984', 22.50, 2),
('Poems', 15.00, 3),
('SQL Basics', 40.00, 4),
('Python Guide', 30.00, 5);

-- 4. ჩანაწერის განახლება (UPDATE)
UPDATE Books 
SET Price = 25.00 
WHERE BookID = 1;

-- 5. გაერთიანებული ცხრილების დაბეჭდვა (JOIN)
SELECT 
    Books.BookID,
    Books.Title,
    Books.Price,
    Authors.FirstName,
    Authors.LastName
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID;

-- 6. ყველა ჩანაწერის წაშლა (DELETE)
DELETE FROM Books;
DELETE FROM Authors;

-- 7. ცხრილების წაშლა (DROP)
DROP TABLE Books;
DROP TABLE Authors;