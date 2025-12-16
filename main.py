import sys
from stats import get_num_words, get_char_count, sort_characters


def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    char_counts = get_char_count(book_text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()
