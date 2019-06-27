import enchant

def numIncorrect(word):
    """
    @param words_in_file - an iterable of words in the current students submission.
    @return - the number of misspelled words in this submission.
    """
    word_dict = enchant.Dict("en_US")
    count = 0
    for word in word:
        if not word_dict.check(word):
            count +=1
            print(word)
    print(count)


def main():
    huge_list = []
    with open('bewertung.txt', "r") as f:
        for line in f:
            huge_list.extend(line.split())
        print(huge_list)
        numIncorrect(huge_list)


if __name__ == '__main__':
    main()

