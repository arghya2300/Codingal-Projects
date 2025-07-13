CREATE TABLE IF NOT EXISTS Resturant (
    NAME TEXT,
    NEIGHBOURHOOD TEXT,
    CUISINE TEXT,
    REVIEW REAL,
    PRICE TEXT,
    HEALTH TEXT
);

INSERT INTO Resturant (NAME, NEIGHBOURHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
  ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
  ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
  ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
  ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
  ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');



SELECT * FROM Resturant;

SELECT DISTINCT CUISINE FROM Resturant;

SELECT * FROM Resturant WHERE  CUISINE = 'Chinese';

SELECT * FROM Resturant WHERE REVIEW >= 4;

SELECT * FROM Resturant WHERE CUISINE = 'Italian' AND PRICE = '$$$';

SELECT * FROM Resturant WHERE NAME LIKE '%Candy%';

SELECT * FROM Resturant ORDER BY REVIEW DESC LIMIT 4;