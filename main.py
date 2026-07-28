from src.extract import extract_books
from src.transform import (
    transform_books,
    check_data_quality
)
from src.database import (
    connect_database,
    create_tables,
    insert_data,
    check_loaded_data
)
from src.reports import run_reports


def main():
    print("Gutendex ETL Pipeline Started")

    all_books = extract_books()

    books_df, categories_df = transform_books(
        all_books
    )

    check_data_quality(
        books_df,
        categories_df
    )

    conn = connect_database()

    create_tables(conn)

    insert_data(
        conn,
        books_df,
        categories_df
    )

    check_loaded_data(conn)

    run_reports(conn)

    conn.close()
    print("\nDatabase  closed")

    print("\nGutendex ETL Pipeline  Finished")


if __name__ == "__main__":
    main()