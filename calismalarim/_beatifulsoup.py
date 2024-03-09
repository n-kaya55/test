html_doc=""""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

<h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

</body>
</html>
"""


from bs4 import BeautifulSoup

soup= BeautifulSoup(html_doc,'html.parser')

result=soup.prettify()  #html dokumanini düzenleme islemi yapar

result=soup.title
result=soup.head
result=soup.title.name  #title
result=soup.title.string  #İlk web sayfam

result=soup.h1 #<h1 id="header">  **1 tane h1 etiketi var**
                # Python Kursu
               #  </h1> 

result=soup.h2 # ilk h2 yi getirir.
result=soup.h2.name #h2
result=soup.h2.string  # Programlama

result=soup.find_all('h2') # sayfada buldugu tum h2 getirir 

result=soup.find_all('h2')[2] #3. h2 geldi

result=soup.div
result=soup.find_all('div')
result=soup.find_all('div')[1] #2. div geldi
result=soup.find_all('div')[1].ul #2. div icindeki ul etiketi geldi

result= soup.div.findChildren()
result=soup.div.findNextSibling().findNextSibling() #sibling ilerliyor 
 

print(result)