#Nathan Raia

def main():
    inputCensor = input("Enter the name of the censored words file: ")
    inputSentence = input("Enter the name of the file to censor: ")
    censorFile = open(inputCensor , "r")
    sentence = open(inputSentence , "r")

    censoredWords = censorFile.read().split(" ")
    words = sentence.read().split(" ")

    for i in censoredWords:
        for j in range(0 , len(words)):
            if i == words[j]:
                words[j] = "*" * len(i)

    censorFile.close()
    sentence.close()
    sentence = open(inputSentence , "w")

    for i in words:
        sentence.write(i)
        sentence.write(" ")

    sentence.close()

main()