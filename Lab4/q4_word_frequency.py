"""Q4 - Word frequency counter using dictionaries only."""


def analyse_text(paragraph, top_n):
    # Keep letters/digits and whitespace; replace punctuation with spaces.
    cleaned = "".join(
        char.lower() if char.isalnum() or char.isspace() else " "
        for char in paragraph
    )
    words = cleaned.split()
    if not words:
        print("No words were entered.")
        return

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print("Counts:", counts)
    top_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    print(f"Top {top_n}:", top_words[:top_n])
    print("Words appearing once:",
          sorted([word for word, count in counts.items() if count == 1]))

    inverted = {}
    for word, count in counts.items():
        inverted.setdefault(count, []).append(word)
    for word_list in inverted.values():
        word_list.sort()
    print("Inverted frequency dictionary:", inverted)

    by_length = {}
    for word in counts:
        by_length.setdefault(len(word), []).append(word)
    for word_list in by_length.values():
        word_list.sort()
    print("Words grouped by length:", by_length)

    search_word = input("Search for a word: ").strip().lower()
    print(f"{search_word}: {counts.get(search_word, 'not found')}")


def main():
    paragraph = input("Enter a paragraph: ")
    if not paragraph.strip():
        print("Please enter some text; the paragraph is empty.")
        return
    try:
        top_n = int(input("Enter N for top N words: "))
        if top_n < 0:
            print("N cannot be negative.")
            return
    except ValueError:
        print("N must be an integer.")
        return
    analyse_text(paragraph, top_n)


if __name__ == "__main__":
    main()
