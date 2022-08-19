def translate_text(sentence):
    # Now reverse the sentence
    sentence = sentence[::-1]
    # if the first letter is a mark, move it to the end
    if sentence[0] in [".", ",", "!", "?"]:
        sentence = sentence[1:] + sentence[0]
        # Lowercase only the second last letter
        sentence = sentence[:-2] + sentence[-2].lower() + sentence[-1]
        # else, lowercase only the last letter
    else:
        sentence = sentence[:-1] + sentence[-1].lower()
    # capitalize the first letter
    sentence = sentence[0].upper() + sentence[1:]
    # replace the marks
    sentence = sentence.replace(" ,", ", ")
    sentence = sentence.replace(" !", "! ")
    sentence = sentence.replace(" ?", "? ")
    sentence = sentence.replace(" .", ". ")
    # Now go through each word and if it contains two quotes, reverse the word
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i].count("'") == 2:
            words[i] = words[i][::-1]
    sentence = " ".join(words)
    sentence = sentence.replace("'", "")
    return sentence


def translate_file(source, output):
    with open(source, 'r', encoding='utf-8') as file:
        text = file.read()
        text = translate_text(text)
        with open(output, 'w', encoding='utf-8') as file:
            file.write(text)
        file.close()


translate_file("C:/Users/Bence/Downloads/Input.txt",
               "C:/Users/Bence/Downloads/Output.txt")

text = "File translation to 'Naisrever' was successfully completed!"
result = translate_text(text)
print(result)
