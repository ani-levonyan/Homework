# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

books = {'title1': 'author1', 'title2': 'author2', 'title3': 'author3'}


def find_author_by_title(title_name: str) -> str:
    for i in books:
        if i == title_name:
            return books[title_name]
    return "Title not found"


print(find_author_by_title("title3"))
