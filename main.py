BOOK_PATH = "books/frankenstein.txt"

def main():
    content = get_book_content(BOOK_PATH)
    word_count = get_word_count(content)
    char_dict = get_character_count_dict(content)

    # Print summary
    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{word_count} words found in the document")
    print()
    print_char_dict(char_dict)
    print("--- End report ---")


def get_book_content(path):
    """Reads and returns the entire contents of a file at the given path."""
    with open(path) as f:
        return f.read()

def get_word_count(content):
    """Returns the number of words in the given text content."""
    words = content.split()
    return len(words)

def get_character_count_dict(content):
    """Creates a dictionary counting occurances of each character in the text."""
    char_count = {}
    words = content.split()
    for word in words:
        for char in word:
            if char.lower() in char_count:
                char_count[char.lower()] += 1
            else:
                char_count[char.lower()] = 1
    return char_count

def get_alphs(char_dict):
    """Filters character dictionary to only include alphabet characters."""
    return {char: count for char, count in char_dict.items() if char.isalpha()}

def sort_dict_by_count(char_dict):
    """Converts character dictionary to sorted list of dicts ordered by count."""
    char_list = [{"char": char, "count": count} for char, count in char_dict.items()]
    char_list.sort(reverse=True, key=(lambda x: x["count"]))
    return char_list


def print_char_dict(char_dict):
    """Prints character counts for each alphabet character in descending order."""
    only_alphs = get_alphs(char_dict)
    sorted_alphs = sort_dict_by_count(only_alphs)

    for char_dict in sorted_alphs:
        char, count = char_dict["char"], char_dict["count"]
        print(f"The '{char}' character was found {count} times")

if __name__ == "__main__":
    main()
