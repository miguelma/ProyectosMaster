import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import xml.etree.ElementTree as ET
import requests
import json
import zipfile

file_name = 'hidro.csv'
df = pd.read_csv(file_name, parse_dates=True, sep=';', encoding = "ISO-8859-1")

plt.figure(figsize=(10, 6))
plt.plot(df['VALUE'][(df['ABBREVIATION']=="LIMEN")&(df['ï»¿STATION_ID']=="HD073085")], linewidth=2)
plt.ylabel('Parámetro LIMEN en la estación HD073085')
plt.xlabel('Tiempo (h)')
plt.savefig('hidro.png')

plt.show()