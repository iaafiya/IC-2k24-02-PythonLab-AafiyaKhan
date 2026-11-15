"""Q3 - Library records with issue/return rules."""

books = {
    "B1": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued_to": []},
    "B2": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued_to": []},
    "B3": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued_to": []},
}


def add_book():
    isbn = input("ISBN: ").strip()
    try:
        copies = int(input("Number of copies to add: "))
        if copies <= 0:
            print("Copies must be positive.")
            return
    except ValueError:
        print("Enter a whole number of copies.")
        return
    if isbn in books:
        books[isbn]["copies"] += copies
        print("Copies updated.")
    else:
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        books[isbn] = {"title": title, "author": author,
                       "copies": copies, "issued_to": []}
        print("Book added.")


def issue_book():
    isbn = input("ISBN: ").strip()
    member = input("Member ID: ").strip()
    if isbn not in books:
        print("Book not found.")
        return
    book = books[isbn]
    if member in book["issued_to"]:
        print("This member already holds this book.")
        return
    member_books = [
        code for code, item in books.items() if member in item["issued_to"]
    ]
    if len(member_books) >= 2:
        print("Issue rejected: member has reached the 2-book limit.")
        return
    if book["copies"] <= 0:
        print("Issue rejected: no copies left.")
        return
    book["copies"] -= 1
    book["issued_to"].append(member)
    print("Book issued successfully.")


def return_book():
    isbn = input("ISBN: ").strip()
    member = input("Member ID: ").strip()
    if isbn not in books:
        print("Book not found.")
        return
    book = books[isbn]
    if member not in book["issued_to"]:
        print("Return rejected: this member does not hold this book.")
        return
    book["issued_to"].remove(member)
    book["copies"] += 1
    print("Book returned successfully.")


def reports():
    author = input("Author to search: ").strip().casefold()
    by_author = {
        isbn: book["title"] for isbn, book in books.items()
        if book["author"].casefold() == author
    }
    print("Books by author:", by_author)

    # Invert book -> issued member IDs into member -> list of book IDs.
    member_books = {}
    for isbn, book in books.items():
        for member in book["issued_to"]:
            member_books.setdefault(member, []).append(isbn)
    print("Members holding more than one book:", {
        member: titles for member, titles in member_books.items()
        if len(titles) > 1
    })
    print("Currently unavailable:", {
        isbn: book["title"] for isbn, book in books.items()
        if book["copies"] == 0
    })
    print("Never issued:", {
        isbn: book["title"] for isbn, book in books.items()
        if not book["issued_to"]
    })


def main():
    while True:
        print("\n--- LIBRARY SYSTEM ---")
        print("1. Add book\n2. Issue book\n3. Return book\n4. Search\n5. Reports\n6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            isbn = input("ISBN: ").strip()
            print(books.get(isbn, "Book not found"))
        elif choice == "5":
            reports()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
