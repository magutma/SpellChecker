import enchant

def numIncorrect(huge_list):
    """
    @param words_in_file - an iterable of words in the current students submission.
    @return - the number of misspelled words in this submission.
    """
    listmisspelled =[]
    word_dict = enchant.Dict("en_US")
    count = 0
    for i in huge_list:
        if not word_dict.check(i):
            count +=1
            listmisspelled.append(i)
    print(listmisspelled)
    print(count)


def main():
    #huge_list = ["dog", "mouse", "cat", "dooog","couldn’t", 'didn’t', 'we’d',"that's",'it’s',"wife’s",'it’s']
    huge_list = ['We','Neapolitan', 'Sorrento',"Aminta","april","OK","didn't", 'stayed', 'aaat', 'the', 'Grand', 'Aminta', 'for', 'seven', 'days', 'the', 'hotel', 'was', 'beautifully', 'clean', 'and', 'the', 'restaurant', 'equally', 'smart', 'The', 'food', 'was', 'a', 'little', 'bland', 'and', 'the', 'service', 'a', 'little', 'rushed', 'It’s', 'glorious', 'position', 'overlooks', 'the', 'beautiful', 'bay', 'below', 'There', 'is', 'a', 'small', 'winding', 'pathway', 'leading', 'down', 'to', 'the', 'town', 'and', 'it', 'takes', '20', 'minutes', 'to', 'do', 'the', 'walk', 'Use', 'the', 'hotel’s', 'shuttle', 'bus', 'to', 'go', 'back', 'up', 'to', 'the', 'hotel', 'as', 'the', 'road', 'up', 'is', 'too', 'dangerous', 'to', 'walk', 'on', 'The', 'plastic', 'glasses', 'in', 'the', 'room', 'are', 'flimsy', 'and', 'not', '4', 'star', 'No', 'kettle', 'is', 'provide', 'so', 'we', 'suggest', 'you', 'take', 'your', 'own', 'Nor', 'do', 'they', 'provide', 'shower', 'gel', 'just', 'a', 'bar', 'of', 'soap']

    numIncorrect(huge_list)


if __name__ == '__main__':
    main()

