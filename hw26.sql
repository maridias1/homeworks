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
(1, 'Galaktion', 'Tabidze'),
(2, 'William', 'Shakespeare'),
(3, 'Fyodor', 'Dostoevsky'),
(4, 'Victor', 'Hugo'),
(5, 'George', 'Orwell');

INSERT INTO Books (BookID, Title, PublishedYear, AuthorID) VALUES
(101, 'The Moon of Mtatsminda', 1915, 1),
(102, 'Sonnets', 1609, 2),
(103, 'The Gambler', 1866, 3),
(104, 'The Hunchback of Notre-Dame', 1831, 4),
(105, '1984', 1949, 5);

-- 4
UPDATE Books
SET PublishedYear = 1916
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
