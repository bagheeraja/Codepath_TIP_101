def highest_rated(books: list[dict]) -> str:
    if not books:
        return None
    
    best_book = books[0]

    for book in books[1:]:
        if book["rating"] > best_book["rating"]:
            best_book = book

    return best_book


books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))