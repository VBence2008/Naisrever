def translate(sentence):
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
    # Now go through each word and if it contains two quotes, reverse the word
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i].count("'") == 2:
            words[i] = words[i][::-1]
    sentence = " ".join(words)
    sentence = sentence.replace("'", "")
    return sentence


print(translate("This 'Naisrever' program reverses the order of words in a sentence, and some other things."))
