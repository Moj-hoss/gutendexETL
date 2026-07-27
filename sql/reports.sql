-- 1. Most downloaded books
SELECT id, title, media_type, download_count
FROM books
ORDER BY download_count DESC
LIMIT 10;


-- 2. Number of books[category]
SELECT category, COUNT(*) AS book_count
FROM category
GROUP BY category
ORDER BY book_count DESC;


-- 3. Average downloads[category]
SELECT
    c.category,
    ROUND(AVG(b.download_count), 2) AS average_download_count
FROM category c
JOIN books b
    ON c.book_id = b.id
GROUP BY c.category
ORDER BY average_download_count DESC;


-- 4. Books with more than 3 categories
SELECT
    b.id,
    b.title,
    COUNT(c.category) AS category_count
FROM books b
JOIN category c
    ON b.id = c.book_id
GROUP BY b.id, b.title
HAVING COUNT(c.category) > 3
ORDER BY category_count DESC;


-- 5. Most downloaded book[category]
SELECT
    c.category,
    b.id,
    b.title,
    b.download_count
FROM category c
JOIN books b
    ON c.book_id = b.id
WHERE b.download_count = (
    SELECT MAX(b2.download_count)
    FROM category c2
    JOIN books b2
        ON c2.book_id = b2.id
    WHERE c2.category = c.category
)
ORDER BY c.category;