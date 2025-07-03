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
    list = []
    with open(file_path) as f:
        file_contents = f.read()
    for char in file_contents.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    for key in char_dict:
        if key.isalpha():
            new_dict = {}
            new_dict["char"] = key
            new_dict["num"] = char_dict[key]
            list.append(new_dict)
    print(list)
    return list

def report (data):
    data = char_analysis("books/frankenstein.txt")
    keys = list(data.keys())
    counts = len(data[keys[0]])
    list = []
    for i in range(counts):
        new_dict = {}
        for key in keys:
            new_dict[key] = data[key][i]
        list.append(new_dict)
    return list

print(char_analysis("books/frankenstein.txt"))