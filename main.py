from stats import count_words, get_unique_char, sort_dict, get_pdf_text
import sys

path = sys.argv[1]
extension = path[-3:len(path)]

def get_txt_text(file_path):
    with open(file_path) as file: 
        return file.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    if extension == "txt":
        text = get_txt_text(path)
    elif extension == "pdf":
        print("Note: Etracting pdf text takes a while!")
        text = get_pdf_text(path)
    else:
        print("Only text (.txt) and pdf (.pdf) files are supported at the moment. Please ensure your file has an extension.")
        sys.exit(1)
        

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for entry in sort_dict(get_unique_char(text)):
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()