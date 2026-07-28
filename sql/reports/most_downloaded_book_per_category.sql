SELECT
    c.category,
    b.id,
    b.title,
    b.download_count
FROM category AS c
JOIN books AS b
    ON c.book_id = b.id
WHERE b.download_count = (
    SELECT MAX(b2.download_count)
    FROM category AS c2
    JOIN books AS b2
        ON c2.book_id = b2.id
    WHERE c2.category = c.category
)
ORDER BY c.category;