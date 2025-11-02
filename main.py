from stats import count_words , count_characters, sort_characters
import sys

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    count_characters_dict = count_characters(book_text)
    sorted_dict = sort_characters(count_characters_dict)
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {word_count} total words\n")
    print("-------- Character Count --------\n")
    for item in sorted_dict:
        print(f"{item['chars']}: {item['nums']}\n")
    print("============= END ===============")
    sys.exit(0)
    