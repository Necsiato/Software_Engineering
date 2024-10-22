def word_counter(file):
    words = []
    summa = []
    count = {}

    with open (file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower().split()
            len_line = len(line)
            words.append((line, len_line))

            for word in line:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
        for i, v in words:
            summa.append(v)
        print(f'Всего слов: {sum(summa)}')
    word_max = max(count, key=count.get)
    max_count = max(count.values())
    print(f'Самое популярное слово: {word_max}\nПовторяется: {max_count}')
word_counter('ind1_input.txt')