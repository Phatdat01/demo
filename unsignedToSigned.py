from asyncio.windows_events import NULL
from itertools import count
from pickle import TRUE
from re import I

question=['ai','sao','gì','nào','không']
exclamatory=['nhá','nhé','nha','ok','làm ơn','chào','đây','đó','thôi','biệt']

sentences = {0: "?", 1: "!", 2: "."}

def AddPrunctuation(label,text):
    text=text+sentences[int(label)]
    return text

def TypeSentence(text):
    sen=text.lower().split()
    if set(sen) & set(question):
        return 0
    elif set(sen) & set(exclamatory):
        return 1
    return 2

def Process(text):
    text=text.strip()
    label=TypeSentence(text)
    text=AddPrunctuation(label,text)
    return text



text="        Tôi chỉ vừa mới ăn sáng       "

text=Process(text)
print(text)