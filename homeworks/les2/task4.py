words=input('Ввод слов:\n')
string_n=1
let_n=0
word_len = 1
print(string_n,')',sep='',end=' ')
for let in words:
    if let!=' ':
        if word_len<11:
            print(let, end='')
        word_len += 1
    else:
        word_len=1
        if let_n+1<len(words):
            if words[let_n]==' ' and words[let_n+1]==' ':
                print(end='')
            else:
                print()
                string_n+= 1
                print(string_n,')',sep='',end=' ')
    let_n+=1
