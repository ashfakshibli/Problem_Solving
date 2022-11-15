def getHighestFreq(text):
   
    lowerText=text.lower()

    words=lowerText.split()
    print(words)

    mostUsedWord=""
    mostUsedFreq=0
    for word in words:
        freq=words.count(word)
        print(word, freq)
        if freq > mostUsedFreq:
            mostUsedWord=word
            mostUsedFreq=freq
    return mostUsedWord, mostUsedFreq


poem="Look at me!\nlook at me!\nlook at me NOW!\nIt is fun to have fun"
print(getHighestFreq(poem))

print(getHighestFreq(poem))

