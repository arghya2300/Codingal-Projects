-- Step 1: Create the hacker_news table
CREATE TABLE IF NOT EXISTS hacker_news (
    id INT PRIMARY KEY,
    title TEXT,
    author TEXT,
    score INT,
    num_comments INT,
    date DATE
);

INSERT INTO hacker_news (id, title, author, score, num_comments, date) VALUES
(1, 'The future', 'alice', 350, 120, '2025-07-01'),
(2, 'Rise of Political tension', 'bob', 275, 85, '2025-06-30'),
(3, 'How to make sure there are no errors?', 'carol', 400, 150, '2025-06-29'),
(4, 'Python is easier than SQL', 'dave', 180, 60, '2025-07-02'),
(5, 'Security Risks', 'alice', 220, 110, '2025-06-28'),
(6, 'Future to Mars', 'emma', 310, 130, '2025-07-03'),
(7, '5G and Beyond', 'bob', 260, 90, '2025-07-01'),
(8, 'Clean Code Principles', 'carol', 330, 105, '2025-07-04');

SELECT 
    title,
    author,
    score,
    num_comments,
    date
FROM 
    hacker_news
WHERE 
    num_comments >= 100
ORDER BY 
    score DESC
LIMIT 5;

SELECT 
    author,
    COUNT(*) AS total_articles,
    AVG(score) AS avg_score,
    SUM(num_comments) AS total_comments
FROM 
    hacker_news
GROUP BY 
    author
HAVING 
    COUNT(*) >= 2
ORDER BY 
    avg_score DESC;
