SELECT
    category,
    COUNT(*) AS book_count
FROM category
GROUP BY category
ORDER BY book_count DESC;