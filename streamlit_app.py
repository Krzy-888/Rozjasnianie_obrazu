import streamlit as st
import numpy as np
import cv2
#import os
#import matplotlib.pyplot as plt
#st.image
#st.slider

plik = st.file_uploader("daj obraz")
if plik is not None:
    #st.image(plik)
    st.write(plik.name)
    st.warning("Ok")

    #scierzka = r"./"
#plik_2 = str(plik)
    #calosc = os.path.join(scierzka,plik.name)
    obraz = cv2.imread(plik)
    obraz = cv2.cvtColor(obraz,cv2.COLOR_BGR2RGB)
    st.write(calosc)
    st.write(obraz.shape)
    lewa,prawa = st.columns(2)
    lewa.image(plik)
    for i in range(3):
        hist = cv2.calcHist([obraz],channels = [i], mask = None, histSize = [256], ranges = [0,256])
        plt.plot(hist,color = kolory[i]);
        plt
    prawa.p
    wartosc = st.slider("rozjasnij lub przyciemnij", -100, 100, 0)
    obraz_2 = obraz.copy()

    obraz_3 = obraz_2.copy()
    #nowa koncepcja
    for i in range(obraz_2.shape[0]):
        for j in range(obraz_2.shape[1]):
            for k in range(obraz_2.shape[2]):
                if (obraz_3[i,j,k] + wartosc >= 0) and (obraz_3[i,j,k] + wartosc) <= 255:
                    obraz_3[i,j,k] = obraz_3[i,j,k] + wartosc
                elif obraz_3[i,j,k] + wartosc < 0:
                    obraz_3[i,j,k] = 0
                else:
                    obraz_3[i,j,k] = 255


    #obraz_2 = obraz_2 + wartosc



    #cv2.normalize(obraz_2,  obraz_3, 0, 255, cv2.NORM_MINMAX)
    st.image(obraz_3)
    #hist = cv2.calcHist([img_g],channels = [0], mask = None, histSize = [256], ranges = [0,256])
    #kolory = ['r','g','b']
    for i in range(3):
        hist = cv2.calcHist([obraz],channels = [i], mask = None, histSize = [256], ranges = [0,256])
        plt.plot(hist,color = kolory[i]);
    st.balloons()



