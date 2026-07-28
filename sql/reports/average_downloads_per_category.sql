SELECT
    c.category,
    ROUND(
        AVG(b.download_count),
        2
    ) AS average_download_count
FROM category AS c
JOIN books AS b
    ON c.book_id = b.id
GROUP BY c.category
ORDER BY average_download_count DESC;