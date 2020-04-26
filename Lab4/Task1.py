#Задайте строку, присвоив ей значение какого-либо абзаца текста, например из Help- справки любого приложения. Подсчитайте количество предложений в абзаце и количество слов в каждом предложении.
#Ihor Mostovyi
#25.04.2020

def main():
    text = input("Input text: ")
    sentences = text.split(". ")
    for sentence in sentences:
        if sentence == "":
            continue
        words = sentence.split(" ")
        countOfWords = len(words)
        print("Count of words in -", sentence, ":", countOfWords)

    countOfSentences = len(sentences)
    print("Count of sentences:", countOfSentences)

    return None

main()