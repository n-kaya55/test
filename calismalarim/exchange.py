import requests
import json

api_key="120845a3c518493705470859"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz=input("bozulan doviz türü: ") # USD 

alinan_döviz=input("Alinan döviz Türü: ") #TRY

miktar=int(input(f" Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ") )
sonuc=requests.get(api_url+bozulan_doviz) 
sonuc_json=json.loads(sonuc.text)
# print(sonuc_json["conversion_rates"][alinan_döviz])
print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_döviz],alinan_döviz))
print("{0}{1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_döviz], alinan_döviz))