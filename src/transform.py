import pandas as pd


def transform_books(all_books):
    books_data = []
    categories_data = []

    for book in all_books:
        books_data.append({
            "id": book["id"],
            "title": book["title"],
            "media_type": book["media_type"],
            "download_count": book["download_count"]
        })

        for bookshelf in book["bookshelves"]:
            if bookshelf.startswith("Category:"):
                category_name = bookshelf.replace(
                    "Category:",
                    ""
                ).strip()

                categories_data.append({
                    "book_id": book["id"],
                    "category": category_name
                })

    print("Book records:", len(books_data))
    print("Category records:", len(categories_data))

    books_df = pd.DataFrame(books_data)
    categories_df = pd.DataFrame(categories_data)

    print("Books shape:", books_df.shape)
    print("Categories shape:", categories_df.shape)

    print("\nBooks preview:")
    print(books_df.head())

    print("\nCategories preview:")
    print(categories_df.head())

    return books_df, categories_df


def check_data_quality(books_df, categories_df):
    print("\n--- Data Quality Checks ---")

    print(
        "Duplicate book IDs:",
        books_df["id"].duplicated().sum()
    )

    print(
        "Duplicate category records:",
        categories_df.duplicated().sum()
    )

    print("\nMissing values in books:")
    print(books_df.isnull().sum())

    print("\nMissing values in categories:")
    print(categories_df.isnull().sum())

    print("\nBooks information:")
    books_df.info()

    print("\nCategories information:")
    categories_df.info()

    print(
        "\nExtra spaces:",
        (books_df["title"] != books_df["title"].str.strip()).sum(),
        (books_df["media_type"] != books_df["media_type"].str.strip()).sum(),
        (
            categories_df["category"]
            != categories_df["category"].str.strip()
        ).sum()
    )