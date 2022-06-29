import codecs
from dataclasses import replace
import json
from logging import exception
import re
import unicodedata

#Load file json
def LoadDataJson(filename):
    file=open(filename,encoding="utf8")
    jData = json.load(file)
    text=''
    for data in jData['alternative']:
        text=(data['transcript'])
    file.close()
    return text

#function that check isnumeric
def is_digit(word):
    try:
        int(word)
        return True
    except ValueError:
        pass
    return False

#for test
##Process for test data
## in this, we can replace method preplace('   ','. ') by divide object
def EditPara(text):
    #remove white space head and last paragraph
    text=text.strip()
    #Upcase the first char in paragraph and and "." last paragraph
    temp = list(text)
    temp[0]=temp[0].upper()
    text = "".join(temp)
    text+='.'
    # if there are a '\t','   ',... Can let it is "." or "\n"
    # Or consider break time of speech
    round=''
    if ('    ' in text):
        index=text.index('    ')
        while text[index]==' ':
            round+=' '
            index+=1
        temp = list(text)
        temp[index]=temp[index].upper()
        text = "".join(temp)
        text=text.replace(round,'. ')
    return text


#print(text)
#Remove ờ, à, thì là,...
#Undone
def RemoveUnnecessaryWord(text):
    remove=['thì là ','a thì ','ukm ','à thì ','ưm thì ','a a ','ờ thì ']
    for rem in remove:
        if rem in text.lower():
            while rem in text.lower():
                index=text.lower().index(rem)
                tempo=text.lower()
                index=tempo.index(rem)
                if (text[index:index+len(rem)]==text[index:index+len(rem)].capitalize()):
                    temp = list(text)
                    temp[index+len(rem)]=temp[index+len(rem)].upper()
                    text = "".join(temp)

                text=text[:index]+text[index+len(rem):]
    return text

def ConvertDate(text):
    month=' tháng '
    year=' năm '
    for index in range(0,len(text)):
        try:
            if (text.index(month,index)==index):
                dateNum = text[index -1]
                monthNum = text[index + len(month)]
                if is_digit(dateNum) and is_digit(monthNum):
                    text=text[:index] + text[index+len(month)-1:]
                    temp = list(text)
                    temp[index]='/'
                    text = "".join(temp)
        except Exception as e:
            if str(e) in 'substring not found':
                pass
            else:
                raise e
        try:
            if (text.index(year,index)==index):
                monthNum = text[index -1]
                yearNum = text[index + len(year)]
                if is_digit(monthNum) and is_digit(yearNum):
                    text=text[:index] + text[index+len(year)-1:]
                    temp = list(text)
                    temp[index]='/'
                    text = "".join(temp)
        except Exception as e:
            if str(e) in 'substring not found':
                pass
            else:
                raise e
    return text

testData=LoadDataJson('1.json')
#testData='        tất cả chú ý        nếu a a mình không có. A a tiền thì mình sẽ không được ổn định   '
text=EditPara(testData)
text=RemoveUnnecessaryWord(text)
text=ConvertDate(text)
print(text)
