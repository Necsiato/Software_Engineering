import re
def new_text(old_text, ban_word):
    for word in ban_word:
        sample = re.compile(re.escape(word), re.IGNORECASE)
        old_text = sample.sub('*' * len(word), text)
    return old_text
text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
with open('ind4_input.txt', 'r') as file:
    ban_word = file.read().strip().split()
result = new_text(text, ban_word)
print(result)