import requests


def extract_books():
    all_books = []

    for page in range(1, 6):
        url = f"https://gutendex.com/books/?page={page}"

        response = requests.get(url)

        page_data = response.json()
        books = page_data["results"]

        all_books.extend(books)

        print(f"Pagee {page}: {len(books)} books")

    print("Total books:", len(all_books))

    return all_books