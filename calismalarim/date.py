#datetime classından sadece istediğin methodları import edebilirsin
from datetime import datetime
# from datetime import time
# from datetime import date

#tüm datetime methodlarını getir
#import datetime


# datetime classındaki methodları listeyebilirsin
simdi=datetime.now()
bugun=datetime.today()
result=simdi.year
result=simdi.month
result=simdi.minute
#ctime daha detayli bilgi donuyor
result=datetime.ctime(simdi)
result=datetime.strftime(simdi,'%Y') # sadece yıl bilgisini donuduru
result=datetime.strftime(simdi,'%X') #sadece saat bilgisini dondurur
result=datetime.strftime(simdi,'%d') #sadece gun bilgisi
result=datetime.strftime(simdi,'%A') #gun bilgisini yazi olarak doner
result=datetime.strftime(simdi,'%B') #ay bilgisini yazi olarak verdi
result=datetime.strftime(simdi,'%Y %A %B') #birden fazla deger cagırabiliyoruz

t='21 Nisan 2023 hour 10:12:30'
result=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')


print(result)