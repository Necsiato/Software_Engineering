sentence = input("Enter a sentence: ")

print("length of the sentence: ", len(sentence))
print("lowercase: ", sentence.lower())

vowels = "aeiou"
print("count of vowels: ",sum(1 for i in sentence.lower() if i in vowels))

print("replacement: ", sentence.replace("ugly", "beauty"))

start = sentence.startswith("The")
end = sentence.endswith("end")
print("Starts with 'The':", start)
print("Ends with 'end':", end)