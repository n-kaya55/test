import re


str="Python Kursu: Python Programlama 100 Puan"
result=re.findall("Python",str)   # ['Python', 'Python']
result=len(result) # kac tane python buldu?

result=re.split(" " , str) #['Python', 'Kursu:', 'Python', 'Programlama', '100', 'Puan']

result=re.sub(" ","-",str) #Python-Kursu:-Python-Programlama-100-Puan (substring) 
result=re.sub("\s","-",str) #Python-Kursu:-Python-Programlama-100-Puan

result=re.search("Python",str) #<re.Match object; span=(0, 6), match='Python'> buldugu ilk python ı donuyor
#result=result.span() #sadece konumunu cekebilirsin!! (0, 6)

#result=result.start() #kacıncı karakterden basladıgını soyler 0
#result=result.end() #6
#result=result.group() #Python
#result=result.string #hangi ifadenin icinde arıyor? "Python Kursu: Python Programlama 100 Puan"

#regular expression

"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]  0 dan 3 e kdr aralik + 9 a bakar 0dan 39a kdr bakmaz!! 

         [^abc] => abc dişindaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""
result=re.findall("[abc]",str)
result=re.findall("[Puan]",str) #['P', 'n', 'u', 'u', 'P', 'n', 'P', 'a', 'a', 'a', 'P', 'u', 'a', 'n']
result=re.findall("[a-e]",str)
result=re.findall("[^0-9]",str) #rakamlar haric!

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match 2 basamak yok
              ab   : 1 match 
              abc  : 1 match
              abcd : 2 matches

    
"""

result=re.findall("...",str) #['Pyt', 'hon', ' Ku', 'rsu', ': P', 'yth', 'on ', 'Pro', 'gra', 'mla', 'ma ', '100', ' Pu']
result=re.findall("Py..on",str) #['Python', 'Python']

"""
    ^ - Belirtilen string karakterlerle başliyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""
result=re.findall("^P",str) #kelime kelime bakmıyor tüm stringin ilk harfine bakıyor!

"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""
result=re.findall("n$",str)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""
"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2} iki basamaklı sayilar
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str)


"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""
"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
         axz
         bxz
         cxz
"""



"""
    \ - Özel karakterleri aramamizi sağlar.
        \$a => $ karakterinin arkasina a karakterinin arar. Yani
               $ regular exp. engine tarafindan yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        \APython => Python en basta mı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)

    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""

print(result)











