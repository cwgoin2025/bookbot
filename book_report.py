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
