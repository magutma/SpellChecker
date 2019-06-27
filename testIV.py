import xlsxwriter

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()



def write(list, i):
    # iterating through content list
    content=list
    row = i
    column = 1
    for item in content:
        # write operation perform
        worksheet.write(row, column, item)
        # incrementing the value of row by one
        # with each iteratons.
        column += 1



for i in range(0,6):
    content = ["ankit", "rahul", "priya", "harshita", "sumit", "neeraj", "shivam"]
    print(content)
    write(content,i)


workbook.close()