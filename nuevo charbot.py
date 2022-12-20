# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:02:55 2020

@author: Alan
"""
import random
import re

def chat(word):
    word=re.sub(' +',' ',word)
    if 'mi nombre es' in word:
        word=re.sub('mi nombre es','',word)
        print(word,',que producto buscas?')
        word=input('R:')
        word=word.lower()
        chat(word)
        return
    elif ('hola' in word) and ('mi nombre es' not in  word) :
        print('hola que tal, cual es tu nombre?')
        word=input('R:')
        word=re.sub('mi nombre es','',word)
        print(word,',algun producto que te agrade?')
        return
    elif ('tu dia'in word )or('te va' in word):
        print('My dia es perfecto, y estoy para ayudarte')
        return
    elif ('eres humano'in word)or('que eres'in word)or('te creo'in word)or('quien eres'in word):
        print('mi nombre es chatbot y fui creado por Alan Ortega como soporte para una tienda electronica')
        return
    elif 'tu nombre' in word:
        print('Mi nombre es chatbot')
        return
    elif 'informacion'in word:
        print('ingresa el nombre de los productos  de los que quieres informacion')
        return
    elif ('bye'in word)or('adios'in word)or( 'gracias' in word)or('seria todo'in word)or('fue todo'in word):
        d=['Fue un placer hablar atenderte ','bye, vueleve pronto','Espero que hayas encontrado lo que buscabas']
        print(random.choice(d))
        return
    elif ('ordenar'in word) or('pedir'in word):
        pedido(word)
        return
    if 'tablet' in word:
        print('La tablet es:\n un ipad de iPad Mini Wi-Fi 64 GB Gray con precio de 9000 pesos\nÚnico modelo\n')
    if ('laptop' in word) or ('computador' in word):
        print('Laptop\n MSI GF75 17.3" Gaming Laptop Intel Core i7-9750H 8GB RAM 512GB SSD 120Hz GTX 1650 Aluminum Black \n y el precio es:22,271.75\nÚnico modelo\n')
    if ('celular'in word) or('telefono'in word):
        print('Celular:\nXiaomi Mi Note 10, 128GB/6GB RAM 6.47'' FHD+ Snapdragon 730G, Verde - Version Global Desbloqueado\n precio:9,699.00\nÚnico modelo\n')
    if 'audifono'in word:
        print('Audifonos:\nSony MDR-EX15LPB Audífonos internos, 8 Hz–22 kHz, Negro\n Precio:125\nÚnico modelo\n')
    if ('disco duro'in word) or('discos duros'in word):
        print('Disco duro:\nSeagate STEA2000400 Expansion - Disco duro externo portátil USB 3.0 de 2TB,\n precio:1300\n Único modelo')
    else: 
        print('algun producto que te interese?,quieres ordenar? informacion?')
    return

def pedido(word):
    d=0 
    print('que prodcutos quieres ordenar?')
    word=input('P:')
    word=word.lower()
    word=re.sub(' +',' ',word)
    if 'tablet' in word:
        print('que cantidad de tablet? (solo numeros)')
        s=input('R:')
        f1=(re.findall('[0-9]+',s))
        f=[int(x) for x in f1]
        d+=f[0]*9000
    if ('laptop' in word) or ('computador' in word)or('lapto'in word):
        print('que cantidad  de Laptop(Solo numeros)')
        s=input('R:')
        f1=(re.findall('[0-9]+',s))
        f=[int(x) for x in f1]
        d+=f[0]*22271.75
    if ('celular'in word)or ('telefono'in word):
        print('que cantidad de celulares(solo numeros)')
        s=input('R:')
        f1=(re.findall('[0-9]+',s))
        f=[int(x) for x in f1]
        d+=f[0]*9699
    if 'audifono'in word:
        print('que cantidad de Audifonos(solo numeros)')
        s=input('R:')
        f1=(re.findall('[0-9]+',s))
        f=[int(x) for x in f1]
        d+=f[0]*125       
    if ('disco duro'in word) or('discos duros'in word):
        print('Que cantidad de Discos duros(solo numeros)')
        s=input('R:')
        f1=(re.findall('[0-9]+',s))
        f=[int(x) for x in f1]
        d+=f[0]*1300
    print('la cantidad seria:',d,'pesos')
    print('confirmar compra yes/no')
    s=input('R:')
    s=s.lower()
    if ('y' in s)or('s' in s):
        print('Ingresa tu domicilio:')
        s=input(':')
        print('tu pedido llegara a la direccion',s,'en dos o tres semanas aprox, algun otro producto que te interese??')
    else: 
        print('algun producto de tu interes??')
    return

        

print('hola bienvenido a la tienda de electronica mis productos son\n 1.-Celulares\n 2.-Laptops \n 3.-Tablet \n 4.-Audifonos\n 5.-.Discos Duros \n Envio gratis solo escibe Ordenar para realizar tu pedido ')
orden =False

while 1:
    word=input('P:')
    word=word.lower()
    chat(word)
    if ('bye'in word)or('adios'in word)or( 'gracias por la atencio' in word):
        break
    word=''

