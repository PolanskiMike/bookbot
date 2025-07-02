def word_analysis(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def char_analysis(file_path):
    char_dict = {}
    with open(file_path) as f:
        file_contents = f.read()
    for char in file_contents.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    char_dict.sort(reverse=True, key=char)
    return char_dict

# def report (data):
#     dictionary_list = []
#     for info in data:
