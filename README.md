# selected_3
Books Classification and Search System

an Arabic Question Answering System based on scrapping data from aseer el kotb site: https://www.aseeralkotb.com/

1- we scrapped our data from asser_al_kotb website
2- we preprocessed the data and cleaned it
3- we tried 3 different types of classification which are Logistic Regression, Naive Bayes, and K-nearest Neighbour to know which have the highest accuracy
4- Intent Classification and Prediction for question in the json file
5- Rule Based model
6- extracted keywords from the description based on tfidf of the word to the description 

Files:
1)asser_el_kotob.py

  1-We requested to extract all the data in the site
  2-We used beautiful soup library to extract specific data in the site (Book name - Author - Book Department - Publishing year - Publishing house - Summary of book - Number of pages ) 
  3-We used Ar-Correct to auto correct the summary of books
  4-We stored data it in csv file
  
2)Books Classification-Selected3.ipynb

  1- we preprocess our data by removing our outliers based on the number of pages
  2- we removed the non-arabic books
  3- we have about 55 categories in our data so we reduced them to 12 categories containing the most populer categories and the category "متنوع".
  4- we extracted the features by calculating the tfidf matrix manually
  5- we made dimensionality reduction by using PCA algorithm
  6- we tried 3 different types of classification which are Logistic Regression, Naive Bayes, and K-nearest Neighbour to know which have the highest accuracy
  7- we made list of keywords from the description based on tfidf of the word to the description ,we took 5 words of the most highest tfidf values 
 
3)intents.json
  
  1-We wrote questions that help us to predict question from input
  
4)qa_system.py

  1-We load the json file 
  2-We tokenized words the json file to differentiate classed(tags) from patterns(which have question)
  3-We  stemmed words in the json file 
  4-We train and test the json file 
  5-We used mlpclassifier to fit the train data
  6-We cleaned up the data
  7-We built function: classify to classify question in the json file
  8-We built function: response to classify question in the input and predict which tag is similar with the question in json file
  9-We used tokenization and stopwords for the query
  10-We built function: CounterOfWordInOneDoc to retrieve words in the search input if true
  11-We built function: check_if_string_in_file to check words from search input is exist or not in the data
  12-We used all those function in the main function
  13-We used tkinter library to build GUI
  
5)Books.csv (data we scrapped from the website)
6)list.txt (list of arabic stopwords)

The rest of the files for the old project, so we didn't use it in this phase
