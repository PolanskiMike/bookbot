# def get_book_text(file_path):
#     with open(file_path) as f:
#         file_contents = f.read()
#     return file_contents

def word_analysis(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def main():
    num_words = word_analysis("books/frankenstein.txt")
    print(f"{num_words} words found in the document")

main()
