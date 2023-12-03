if __name__ == '__main__':
    contents = open("day1-1-input.txt", "r").read()
    result = []
    words = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    words_to_number = {word: number for word, number in zip(words, range(1, len(words)+1)) }

    for s in contents.split():
        current_strings = []
        current_str = s
        replacements = []
        for word, number in words_to_number.items():
            position = current_str.find(word)
            if position != -1:
                replacements.append((position, word))

        if replacements:
            replacements.sort(key=lambda x: x[0])
            for _, word in replacements:
                current_str = current_str.replace(word, str(words_to_number[word]))

        for c in current_str:
            if c.isdigit():
                current_strings.append(c)
                break
        for c in current_str[::-1]:
            if c.isdigit():
                current_strings.append(c)
                break

        # print(current_strings)
        # print(result)
        result.append(int((''.join(current_strings))))

    print(sum(result))
