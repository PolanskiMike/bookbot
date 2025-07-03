from stats import word_analysis
from stats import char_analysis

def main():
    book_path = "books/frankenstein.txt"
    num_words = word_analysis(book_path)
    print(f"{num_words} words found in the document")
    print(char_analysis(book_path))

main()
