#METOZU IZMANTOSANA

#---open() = atver failu
datne=open("txt/admin.txt")

#---readline() = izlasa pirmo rindu
#print(datne.readline())

#---readlines() = izlasa parejas rindas
#print(datne.readlines())

#---split() = atdala rindu
sum=0
for rinda in datne:
  print("rinda=",rinda)
  sarakstaDati=rinda.split(" ")
  vards=sarakstaDati[0]
  print("vards=",vards)
datne.close()
