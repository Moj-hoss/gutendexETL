SELECT
    b.id,
    b.title,
    COUNT(c.category) AS category_count
FROM books AS b
JOIN category AS c
    ON b.id = c.book_id
GROUP BY
    b.id,
    b.title
HAVING COUNT(c.category) > 3
ORDER BY category_count DESC;