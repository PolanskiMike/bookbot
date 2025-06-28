def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_analysis(file_contents):
    file_contents = "books/frankenstein.txt".split()
    count = 0
    for char in file_contents:
        count += 1
    print(f"{count} words found in the document.")

def main():
    print(get_book_text("books/frankenstein.txt"))

word_analysis("books/frankenstein.txt")

