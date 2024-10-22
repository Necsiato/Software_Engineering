def stats():
    with open('ind3_input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.count('\n') + 1
    words = len(text.split())
    letters = sum(1 for char in text if char.isalpha())

    print(f'{letters} символов')
    print(f'{words} слов')
    print(f'{lines} строк')

stats()