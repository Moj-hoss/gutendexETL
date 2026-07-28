# Gutendex ETL Project

This project gets book data from the Gutendex API.

The first 5 pages of the API are extracted.

The data is transformed and saved in a SQLite database.

The project is divided into separate modules for extraction, transformation, database operations, and reports.

## Saved Book Data

The `books` table contains:

* id
* title
* media_type
* download_count

The `category` table contains:

* book_id
* category

## SQL Reports

The project includes these reports:

1. Most downloaded books
2. Number of books in each category
3. Average downloads in each category
4. Books with more than 3 categories
5. Most downloaded book in each category

The SQL queries are in:

```text
sql/reports/
```

## Data Visualization

The notebook includes two charts:

1. Most downloaded books
2. Top 10 categories by number of books

## Project Files

```text
main.py
src/extract.py
src/transform.py
src/database.py
src/reports.py
```

## Run the Project

Install the packages:

```bash
pip install -r requirements.txt
```

Run the ETL pipeline:

```bash
python main.py
```

The original notebook, including the charts, is available in:

```text
Gutendex.ipynb
```
