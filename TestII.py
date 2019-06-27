from spellchecker import SpellChecker

spell = SpellChecker()

spell.word_frequency.load_text_file("C:/Users/Matthias/PycharmProjects/Test/bewertung.txt")

def numIncorrect(list):
    misspelled = spell.unknown(list)
    for word in misspelled:
        print(word)


def main():
    spell.word_frequency.load_text_file("C:/Users/Matthias/PycharmProjects/Test/bewertung.txt")
    huge_list = []
    with open('bewertung.txt', "r") as f:
        for line in f:
            line = line.replace('\n', '').replace('[', '').replace(']', '').replace('.', '').replace(",", "")
            huge_list.extend(line.split())
        #print(huge_list)
        numIncorrect(huge_list)


if __name__ == '__main__':
    main()
