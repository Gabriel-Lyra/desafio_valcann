import os

def insert_header(originalfile, string):
    with open(r'C:\Users\gabri\Desktop\atividade_valcann\books_update_temp.csv','r', encoding='utf8') as f:
        with open(r'C:\Users\gabri\Desktop\atividade_valcann\books_update.csv','w', encoding='utf8') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.remove(r'C:\Users\gabri\Desktop\atividade_valcann\books_update_temp.csv')
    # add later remove books
    # add later remove books_complete


# add later download books_complete

with open(r'C:\Users\gabri\Desktop\atividade_valcann\books.csv', 'r', encoding='utf8') as t1, open(r'C:\Users\gabri\Desktop\atividade_valcann\books_complete.csv', 'r', encoding='utf8') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open(r'C:\Users\gabri\Desktop\atividade_valcann\books_update_temp.csv', 'w', encoding='utf8', newline='') as outFile:
    for line in fileone:
        if line not in filetwo:
            outFile.write(line)

insert_header(r'C:\Users\gabri\Desktop\atividade_valcann\books_update_temp.csv', 'Title\tCategory\tStock\tStars\tPrice\n')