SELECT
    id,
    title,
    media_type,
    download_count
FROM books
ORDER BY download_count DESC
LIMIT 10;