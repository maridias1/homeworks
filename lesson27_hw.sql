-- ==========================================
-- 1. მონაცემთა ბაზის შექმნა და არჩევა
-- ==========================================
CREATE DATABASE lesson27_hw;
USE lesson27_hw;


-- ==========================================
-- 2. ცხრილების შექმნა შესაბამისი დიზაინით (ტიპებით) და მონაცემების შევსება
-- ==========================================

-- sea_lions ცხრილის შექმნა
CREATE TABLE sea_lions (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    species VARCHAR(100)
);

-- sea_lions ცხრილის შევსება მონაცემებით
INSERT INTO sea_lions (id, name, species) VALUES
(10484, 'Ayah', 'Zalophus californianus'),
(11728, 'Spot', 'Zalophus californianus'),
(11729, 'Tiger', 'Zalophus californianus'),
(11732, 'Mabel', 'Zalophus californianus'),
(11734, 'Rick', 'Zalophus californianus'),
(11790, 'Jolee', 'Zalophus californianus');


-- migrations ცხრილის შექმნა
CREATE TABLE migrations (
    id INT,
    distance INT,
    days INT
);

-- migrations ცხრილის შევსება მონაცემებით
INSERT INTO migrations (id, distance, days) VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52),
(11737, 1957, 92);


-- ==========================================
-- 3. JOIN ოპერაციები და შედარება
-- ==========================================

-- 3.1. INNER JOIN (ან უბრალოდ JOIN)
-- აბრუნებს მხოლოდ იმ ჩანაწერებს, რომლებიც ორივე ცხრილში ემთხვევა (5 ჩანაწერი)
SELECT * 
FROM sea_lions s
JOIN migrations m ON s.id = m.id;


-- 3.2. LEFT JOIN
-- აბრუნებს მარცხენა ცხრილის ყველა ჩანაწერს (6 ჩანაწერი, დაემატა Jolee-11790 NULL-ებით)
SELECT * 
FROM sea_lions s
LEFT JOIN migrations m ON s.id = m.id;


-- 3.3. RIGHT JOIN
-- აბრუნებს მარჯვენა ცხრილის ყველა ჩანაწერს (8 ჩანაწერი, დაემატა 11735, 11736, 11737 NULL-ებით)
SELECT * 
FROM sea_lions s
RIGHT JOIN migrations m ON s.id = m.id;


-- 3.4. FULL JOIN — UNION-ის გამოყენებით
-- აერთიანებს ორივე ცხრილს და წაშლის დუბლიკატებს (9 უნიკალური ჩანაწერი)
SELECT * FROM sea_lions s LEFT JOIN migrations m ON s.id = m.id
UNION
SELECT * FROM sea_lions s RIGHT JOIN migrations m ON s.id = m.id;


-- 3.5. FULL JOIN — UNION ALL-ის გამოყენებით
-- აერთიანებს ორივე ცხრილს დუბლიკატების წაშლის გარეშე (14 ჩანაწერი)
SELECT * FROM sea_lions s LEFT JOIN migrations m ON s.id = m.id
UNION ALL
SELECT * FROM sea_lions s RIGHT JOIN migrations m ON s.id = m.id;