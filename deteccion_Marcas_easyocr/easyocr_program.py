from pandas.io.excel import ExcelWriter
import pandas as pd
import os
import easyocr
import cv2
import re
import matplotlib.pyplot as plt
import matplotlib.image as img
##
df = pd.DataFrame([],columns=['Hora','Marca'])
##funcion del tiempo
def format_Hora(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
##
reader = easyocr.Reader(["es"], gpu=False)
input_image="/content/Captures"
file_text=os.listdir(input_image)
print(file_text)
##bandera de reconocimiebto
b_geico=0
b_stubhub=0
count=0  #contador de frames
cont_geico=0 #contador para marca Geico
cont_stubhub=0 #contador marca StubHub
fr_seg=1 #frames por segundo 1/frames 
##
for i  in file_text:
     image = img.imread(input_image+'/'+i)
     result = reader.readtext(image, paragraph=False)
     for res in result:
       c=res[1]
       c=re.sub(' ','',c)
       c=c.lower()
       if (('geico'in c) or ('stubhub' in c)):
         pt0 = res[0][0]
         pt1 = res[0][1]
         pt2 = res[0][2]
         pt3 = res[0][3]
         cv2.rectangle(image, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
         cv2.putText(image, res[1], (pt0[0], pt0[1] -3), 2, 0.8, (255, 255, 255), 1)
         cv2.rectangle(image, pt0, pt2, (166, 56, 242), 2)
       if ('geico'in c):
         b_geico=1
       else: 
         b_stubhub=1
     plt.imshow(image)
     plt.show()
     if (b_geico==1):
       df = df.append({'Hora':format_Hora(count*fr_seg),'Marca':'Geico'},ignore_index=True)
       cont_geico=cont_geico+1
     if (b_stubhub==1):
       df = df.append({'Hora':format_Hora(count*fr_seg),'Marca':'StubHub'},ignore_index=True)
       cont_stubhub=cont_stubhub+1
     count=count+1
     b_geico=0
     b_stubhub=0
df = df.append({'Hora':'Total time Geico','Marca':'Totaltime StubHub'},ignore_index=True)
df = df.append({'Hora':format_Hora(cont_geico*fr_seg),'Marca':format_Hora(cont_stubhub*fr_seg)},ignore_index=True)
writer = ExcelWriter('/content/ejemplo.xlsx')
df.to_excel(writer,'Reporte', index=False)
writer.save()