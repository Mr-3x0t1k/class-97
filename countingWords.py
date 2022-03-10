ets = input("Enter The Sentence: ")
charectarCount = 0
wordCount = 1
for i in ets:
    charectarCount = charectarCount+1
    if(i == ' '):
        wordCount = wordCount+1
print("number of words in the sentence is =")
print(wordCount)
print("number of charectars in the sentence is =")
print(charectarCount)