def sort_on(counts):
    """
    Sort the char_count dictionary in reverse order
    :param counts: dictionary: dictionary containing the character counts for the book
    :return: dictionary containing the character counts from greatest to smallest
    """
    return {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

def report_all(file_path, word_count, character_counts):
    """
    Report the findings in a pretty format
    :param file_path: string: path to the book being analyzed
    :param word_count: integer: Count of the words in the book
    :param character_counts: dictionary: dictionary with character counts
    :return: None
    """
    title_banner = "============ BOOKBOT ============"
    word_count_banner = "----------- Word Count ----------"
    char_count_banner = "--------- Character Count -------"
    end_banner = "============= END ==============="
    sort_chars = sort_on(character_counts)
    print(title_banner)
    print(f"Analyzing book found at {file_path}...")
    print(word_count_banner)
    print(f"Found {word_count} total words")
    print(char_count_banner)
    for char in sort_chars:
        if char.isalpha():
            print(f"{char}: {sort_chars[char]}")
    print(end_banner)


def get_num_words(book_text):
    """
    get the number of words in a given book text
    :param book_text: str, the text string of a book
    :return: the number of words found in the text
    """
    words = book_text.split()
    word_count = len(words)
    return word_count


def count_chars(book_text):
    """
    Counts the occurrence of each character appears in the text of a book. Note that all letters are converted
    to lower case, such that T = t, C=c, etc.
    :param book_text: str   the text string of a book
    :return: a dictionary with a count of each character
    """
    char_dict = {}
    for character in book_text:
        char = character.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
