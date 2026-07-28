import sqlite3


DATABASE_PATH = "data/database/gutendex.db"


def connect_database():
    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    print("\nDatabase connection created.")

    return conn


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS category")
    cursor.execute("DROP TABLE IF EXISTS books")

    cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        media_type TEXT,
        download_count INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE category (
        book_id INTEGER NOT NULL,
        category TEXT NOT NULL,
        PRIMARY KEY (book_id, category),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
    """)

    conn.commit()

    print("Database tables created.")


def insert_data(conn, books_df, categories_df):
    cursor = conn.cursor()

    books_rows = list(
        books_df.itertuples(index=False, name=None)
    )

    category_rows = list(
        categories_df.itertuples(index=False, name=None)
    )

    cursor.executemany("""
    INSERT INTO books (
        id,
        title,
        media_type,
        download_count
    )
    VALUES (?, ?, ?, ?)
    """, books_rows)

    cursor.executemany("""
    INSERT INTO category (
        book_id,
        category
    )
    VALUES (?, ?)
    """, category_rows)

    conn.commit()

    print("Data inserted into the databas")


def check_loaded_data(conn):
    cursor = conn.cursor()

    book_count = cursor.execute(
        "SELECT COUNT(*) FROM books"
    ).fetchone()[0]

    category_count = cursor.execute(
        "SELECT COUNT(*) FROM category"
    ).fetchone()[0]

    print("\n   Loaded Data Check   ")
    print("Books in database:", book_count)
    print("Categories in database", category_count)