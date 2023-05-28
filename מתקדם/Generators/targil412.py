def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_generator = (words[i] for i in sentence.split(" "))
    return " ".join([word for word in translated_generator])

def main():
    print(translate("el gato esta en la casa"))



if __name__ == '__main__':
    main()

