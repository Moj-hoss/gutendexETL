from pathlib import Path

import pandas as pd

REPORTS_DIRECTORY = Path("sql/reports")

REPORTS = [
    (
        "1. Most Downloaded Books",
        "most_downloaded_books.sql"
    ),
    (
        "2. Number of Books per Category",
        "books_per_category.sql"
    ),
    (
        "3. Average Downloads per Category",
        "average_downloads_per_category.sql"
    ),
    (
        "4. Books with More Than Three Categories",
        "books_with_many_categories.sql"
    ),
    (
        "5. Most Downloaded Book per Category",
        "most_downloaded_book_per_category.sql"
    )
]


def load_query(file_name):
    query_path = REPORTS_DIRECTORY / file_name
    return query_path.read_text()


def run_reports(conn):
    for report_title, file_name in REPORTS:
        query = load_query(file_name)
        report = pd.read_sql_query(query, conn)

        print(f"\n{report_title}")
        print(report)