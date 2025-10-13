from stats import count_words, get_unique_char, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as file: 
        return file.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for entry in sort_dict(get_unique_char(text)):
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")


main()