def main():
    word_dictonary = {

        "hi" : "a way of greeting",
        "eyes" : "an organ for seeing",
        "earth" : "a planet in space"

    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictonary:
            print(word,":",word_dictonary[word])

main()