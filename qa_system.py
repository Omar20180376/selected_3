# -*- coding: utf-8 -*-
"""QA_System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bayKZ4lbHek7c84cBjcB5GWEXVZ_hr4y
"""
import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize

import nltk
from nltk.stem.isri import ISRIStemmer
stemmer = ISRIStemmer()
nltk.download('punkt')
import numpy as np
 
import pandas as pd
import random

import json
with open('question.json', encoding="utf-8") as json_data:
    intents = json.load(json_data)

words = []
classes = []
documents = []
ignore_words = ['?']
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)

training = []
output = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

train_x = np.asarray(train_x)
train_y = np.asarray(train_y)

print("Train X :\n",train_x[:5])
print("\nTrain Y :\n",train_y[:5])

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(50),solver='sgd',learning_rate_init=0.01,max_iter=1000)

mlp.fit(train_x, train_y)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1

    return(np.array(bag))

context = {}

ERROR_THRESHOLD = 0.50
def classify(sentence):
    results = mlp.predict([bow(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list

def response(sentence):
    results = classify(sentence)
    if results:
        while results:
            for i in intents['intents']:
                if i['tag'] == results[0][0]:
                    return(i['tag'])

            return results


















def rowDF(fileName,index):
     titanic = pd.read_csv(fileName)
    
     return  titanic.iloc[[index]]
    
    

def readColumnCsv(fileName,column):
    titanic = pd.read_csv(fileName)
    titanic.head()
    columnx = titanic[column]
    columnx=columnx.tolist()
    return columnx


def TokenizationForQuery(Query):
    listLower = []
    word_tokens = regexp_tokenize(Query, "\s|[\.,;'_]", gaps=True)
    for word in word_tokens:
        word.split(word)
        listLower.append(word.lower())
    return listLower

def StopwordQuery(tokenizationList):
    stopwordsapp = nltk.corpus.stopwords.words('arabic')
    filtered_sentence = [w for w in tokenizationList if not w in stopwordsapp]
    filtered_sentence = []
    for w in tokenizationList:
        if w not in stopwordsapp:
            filtered_sentence.append(w)
    return filtered_sentence

def CounterOfWordInOneDoc(bookX, string_to_search):
    newSearch = string_to_search.lower()
     

    if newSearch in bookX:
        n = bookX.count(newSearch)  # 1
        return n
    return 0



def check_if_string_in_file(file_name, string_to_search):
    newSearch = string_to_search.lower()

    if newSearch in file_name:
        return True
    else:
        return False


def list_duplicates_of(List, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = List.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs














from IPython.display import display
    
def main(term):
    
 
    # term = ''
    df=pd.read_csv('Books.csv')
    
    
    counter = 0
    # term = input('Enter term  or query to Search: ')
    res = "من مؤلف"
    
    print(term)
    print(response(term))
    colum=response(term)
    
    term=term.strip()
    word_tokens = TokenizationForQuery(term)
    print(word_tokens)
    word_stopwords = StopwordQuery(word_tokens)
    print(word_stopwords)
    
    columBooks=readColumnCsv('Books.csv',   colum)
    
    for word in word_stopwords:
        count_row=0   
        for book in columBooks:
            
                 counter = counter + CounterOfWordInOneDoc(book, word)
                 
                 count_row+=1
                 if(check_if_string_in_file(book, (word))):
                     print(' in =>   ' + book + "   => " + str(count_row) )
        if(counter!=0):
            print("["+word + "]" + str(counter))
        else:
            term=term.replace(word, '')
        counter=0
    word=term.lstrip()
    count_row=0   
    dataArr=[]
    for book in columBooks:
        
             counter = counter + CounterOfWordInOneDoc(book, word)
             
             count_row+=1
             if(check_if_string_in_file(book, (word))):
                 print(' in =>   ' + book + "   => " + str(count_row) )
                 dataArr.append( df.loc[[count_row-1]].values)
                 display( df.loc[[count_row-1]].values)
    print("["+word + "]" + str(counter))
    counter=0
    print("\n\n\n\n")
    print(dataArr)
    return dataArr
                
            
            

from tkinter import *

  
def findIt():
    global lst
    t.config(state=NORMAL )
    t.delete('1.0',END)
    result=txtfld.get()
    if result=='':
        return None;
    x=main(result)
    
    lst=x
    for v in lst:
        t.insert(END,  str(v)+'\n\n\n'+'------------------------------------------------------------------------------\n\n')
    t.config(state=DISABLED)
    return x

    #مؤلفات طه حسين
 
    
window=Tk()
btn=Button(window, text="Click", fg='blue',command=findIt)

btn.place(x=80, y=100)
lbl=Label(window, text="QA", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="This is Entry Widget", bd=5,width=45)
txtfld.place(x=80, y=180)



t = Text(window,width=190)
t.place(x=20, y=280)

window.title('Hello Python')

window.geometry("1500x700")
window.mainloop()