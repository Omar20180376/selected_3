import requests
from bs4 import BeautifulSoup 
import csv
import pandas as pd
from ar_corrector.corrector import Corrector
corr = Corrector()

# Get the data of book card 
books_name_list = []
books_author_list = []
Books_links_list =[ ]
# Get the detailed data of book card
author_link_list = []
department_link_list = [ ]
language = []
no_pages = []
publishing_house = []
size_of_book = []
type_of_book = []
summary_of_books_list = []

#Clean data
for page_number in range(61,70):
  
    result = requests.get(f"https://www.arab-books.com//page/{page_number}")
    # print result displayed response : 200 succeed 

    src = result.content
    # print(src) will display 

    # to extract data
    soup = BeautifulSoup(src,'lxml')
    #--------------------------------------

    # Get markup tags of required data from site 
    #book names
    #books_name = soup.find_all('h3',{'class':'post-title'})
    #corr.contextual_correct(books_name)
    #print(books_name)
    #----------------------------
    Books_links = soup.find_all('a',{'class':'post-thumb'})
    print(page_number)
    #----------------------------
    #author
    #books_author = soup.find_all('div',{'class':'book-writer'})
    #corr.contextual_correct(books_author)
    #print(books_author)
    #----------------------------

    
    for i in range(  len(Books_links) ):
    
       Books_links_list.append(Books_links[i].attrs["href"])
    
print(len(Books_links_list))   

   
  
xyz=0
# Get data of every link
for link in Books_links_list:
    
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src,"lxml")

    #Get info
    info_of_book = BeautifulSoup(str(soup.find_all("div",attrs={"class":"book-info"})))
    ul = info_of_book.find('ul')
    #ul = BeautifulSoup(info_of_book).find('ul')
    #ul = BeautifulSoup(ul)
    if ul is not None:
      li = ul.find_all("li")
    else: continue
    li = ul.find_all("li")
    a = info_of_book.find_all("a")



    # Get link of author info
    books_author_list.append(a[0].text)
    books_author_list = [item.replace("كتب الكاتب","") for item in books_author_list ]
    #corr.contextual_correct(books_author_list[i])
    # Get link of department 
    
    
    if len(a) > 3:
        department_link_list.append(a[2].text+"-"+a[3].text)
        
    else:
             try:
                 department_link_list.append(a[1].text)
             except IndexError:
                 department_link_list.append('null')
        
    department_link_list = [item.replace("تحميل"," ") for item in department_link_list ]
    department_link_list = [item.replace("اضغط هنا","") for item in department_link_list ]
    # Get the language of the book
    language.append(li[2].text)
    #language = [item.replace("لغة الكتاب:","") for item in language]
    
    #language_list = language.replace("لغة الكتاب:"," ")
    # Get no of pages
    no_pages.append(li[3].text)
    no_pages = [item.replace("عدد الصّفحات:","") for item in no_pages ]
    
    # Get the publishing_house 
    publishing_house.append(li[4].text)
    publishing_house = [item.replace("دار النشر:",'') for item in publishing_house ]
    # Get size of book
    size_of_book.append(li[5].text)
    size_of_book = [item.replace("حجم الكتاب:","") for item in size_of_book]
    # Get type of book
    type_of_book.append(li[6].text)
    xyz+=1
    print(xyz)
    #type_of_book = [item.replace("ملف الكتاب:","") for item in type_of_book]
    #-------------------------------------------------------------------------------
    div_of_sum_books = soup.find("div",{"id":"books-content"})
    p = div_of_sum_books.find_all("p")
    
    if len(p) > 5:
         #corr.contextual_correct(p[2].text+p[3].text)
         summary_of_books_list.append(corr.contextual_correct(p[2].text+p[3].text))
         print('in if######')
    else:
         print('in else')
    #     corr.contextual_correct(p[1].text)
         try:
             summary_of_books_list.append(corr.contextual_correct(p[1].text))
         except IndexError:
              summary_of_books_list.append('null')
    
     #print(summary_of_books_list)        





#file_list = [books_name_list,books_author_list]
#exported = zip_longest(*file_list) # to make data of name inder name and dats of author under author
#with open("sample_data/data.csv","w",encoding="utf-8") as myfile:
 # wr = csv.writer(myfile)
  #wr.writerow(["name","author"])
  #wr.writerows(exported)

df = pd.DataFrame(list(zip(books_author_list,department_link_list,no_pages,publishing_house,size_of_book,summary_of_books_list)),columns =[  'الكاتب',  'قسم الكتاب','عدد الصفحات' , 'دار النشر' , 'حجم الكتاب','تلخيص الكتاب'])
df.to_csv('sample_data/test.csv',index=False,header=True,encoding="UTF-8")