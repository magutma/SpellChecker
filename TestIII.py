from spellchecker import SpellChecker
import xlrd
import xlsxwriter
import enchant
import re
spell = SpellChecker()

#Anpassung

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()


loc = (r"C:\Users\Matthias\Desktop\ErsteErgebnisse\190627_Spellingchecker.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# For row 0 and column 0
sheet.cell_value(0, 0)


def write(misspelled,i, amountmisspelled, amountOfWords ):
    # iterating through content list

    print(misspelled)
    row = i
    column = 1
    worksheet.write(row, column, str(misspelled))
    column+=1
    worksheet.write(row, column, amountmisspelled)
    column+=1
    worksheet.write(row, column, amountOfWords)
    #for item in misspelled:
        # write operation perform
    #    worksheet.write(row, column, item)
        # incrementing the value of row by one
        # with each iteratons.
    #    column += 1
    #column=0


def numIncorrect(list,i,amountOfWords):

    '''misspelled = spell.unknown(list)
    count = 0
    for word in misspelled:
        count += 1
    amountmisspelled = len(misspelled)
    
    write(misspelled,i,amountmisspelled,amountOfWords)
    print(count)
    '''
    listmisspelled = []
    word_dict = enchant.Dict("en_US")
    amountmisspelled = 0
    for j in list:
        if not word_dict.check(j):
            amountmisspelled += 1
            listmisspelled.append(j)
    write(listmisspelled,i,amountmisspelled,amountOfWords)


def splitwords(text,i):
    huge_list = []
    x = text.split()
    for line in x:
        #line = line.replace('\n', '').replace('[', '').replace(']', '').replace('.'," ").replace(",", " ").replace("!"," ").replace("(","").replace(")","").replace("/"," ").replace("-"," ").replace(":"," ").replace(";"," ").replace("?"," ").replace("&"," ").replace("%"," ").replace("£"," ").replace("€"," ")
        line = line.replace('\n', ' ').replace('\t', ' ')#.lower()#ersetzt Zeilenumbrueche und Taps
        line = re.sub('[^\'a-zA-Z]', ' ', line)#ersetzt alles was nicht a-z und ' ist mit leerzeichen
        huge_list.extend(line.split())
    amountOfWords = len(huge_list)
    numIncorrect(huge_list, i, amountOfWords)
    #print(huge_list)



def main():
    #loc = (r"C:\Users\Matthias\Desktop\ErsteErgebnisse\190619_Spellingchecker.xlsx")
    #wb = xlrd.open_workbook(loc)
    #sheet = wb.sheet_by_index(0)
    ## For row 0 and column 0
    #sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        text = (sheet.cell_value(i, 1))
        splitwords(text,i)
        #print(text)


if __name__ == '__main__':
    main()

workbook.close()