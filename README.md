# Gutendex ETL Project

This project gets book data from the Gutendex API.

I used the first 5 pages of the API.

The data is cleaned and saved in a SQLite database.

## Saved Book Data

The `books` table contains:

- id
- title
- media_type
- download_count

The `category` table contains:

- book_id
- category

## SQL Reports

The project includes these reports:

1. Most downloaded books
2. Number of books in each category
3. Average downloads in each category
4. Books with more than 3 categories
5. Most downloaded book in each category

The SQL queries are in:

```text
sql/reports.sql
```

## Run the Project

Install the packages:

```bash
pip install -r requirements.txt
```

Open the notebook:

```text
Gutendex.ipynb
```

Run all cells from top to bottom.