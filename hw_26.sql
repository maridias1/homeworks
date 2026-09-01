-- 1
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL
);

-- 2
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    PublishedYear INT,
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
);

-- 3
INSERT INTO Authors (AuthorID, FirstName, LastName) VALUES
(1, 'Gia', 'Natsvlishvili'),
(2, 'Shota', 'Rustaveli'),
(3, 'Saba', 'Orbeliani'),
(4, 'Ilia', 'Chavchavadze'),
(5, 'Akaki', 'Tsereteli');

INSERT INTO Books (BookID, Title, PublishedYear, AuthorID) VALUES
(101, 'Python Basics', 2023, 1),
(102, 'The Knight in the Panther Skin', 1200, 2),
(103, 'Fables', 1700, 3),
(104, 'Letters of a Traveler', 1861, 4),
(105, 'Bashi-Achuki', 1895, 5);

-- 4
UPDATE Books
SET PublishedYear = 2024
WHERE BookID = 101;

-- 5
SELECT 
    Books.BookID,
    Books.Title,
    Books.PublishedYear,
    Authors.FirstName || ' ' || Authors.LastName AS AuthorName
FROM Books
INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID;

-- 6
DELETE FROM Books;
DELETE FROM Authors;

-- 7
DROP TABLE Books;
DROP TABLE Authors;