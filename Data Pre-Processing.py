# -*- coding: utf-8 -*-
"""10_LENTENG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PV8lhiVLP6hyLpm9gAvDMWKITEh6Ogu2
"""

import pandas as pd
import numpy as np #statdes
import matplotlib.pyplot as plt #vis
import seaborn as sns #vis
import warnings #data besar biasanya python ngasih notice kalo terlalu besar
warnings.filterwarnings('ignore') #noticenya diignore
from matplotlib import rcParams #modifikasi visualisasi
rcParams['figure.figsize'] = 12, 6
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'

"""# Bagian Baru"""

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_excel("/content/10. LENTENG.xls")

data.sample(10)

data.info()

for col in data.columns:
    msg = 'column: {:>10}\t percent of NaN value: {:.2f}%'.format(col, 100 * (data[col].isnull().sum() / data[col].shape[0]))
    print(msg)

data["RT"] = data["RT"].astype('object')
data["RW"] = data["RW"].astype('object')
data["PETUGAS ENTRI"] = data["PETUGAS ENTRI"].astype('object')
data["SURVEYOR"] = data["SURVEYOR"].astype('object')
data["NO URUT"] = data["NO URUT"].astype('object')

data.info()

#menghapus kolom yang banyak unique dan missing values
data.drop(['SURVEI ID','NO. KK','WANITA USIA HAMIL','KETERANGAN BLOK II',
           'KETERANGAN BLOK IV','KETERANGAN KB','KETERANGAN BLOK V','NO. URUT BANGUNAN','NO. URUT KELUARGA'], axis=1, inplace = True)

data.info()

#CLEANING DATA
data.dropna(subset=['NAMA KK'], inplace=True)
data.dropna(subset=['JENIS SUMBER AIR TERLINDUNG'], inplace=True)
data.dropna(subset=['JENIS JAMBAN SANITER'], inplace=True)
data.dropna(subset=['NIK'], inplace=True)

print(data.duplicated().sum())#cek duplicated data
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())

data['KELURAHAN'].value_counts()

!pip install pywedge

import pywedge as pw

dash = pw.Pywedge_Charts(data, c=None, y='MEROKOK')

dashboard = dash.make_charts()

!pip3 install pandas_profiling --upgrade

import pandas_profiling as pp
from pandas_profiling import ProfileReport
pp.ProfileReport(data)

data.to_excel("lenteng.xls", index=False)

data1 = pd.read_excel('lenteng.xls')

data1.head()

df=pd.DataFrame(data1)
data_kepala_keluarga=df.loc[df['HUBUNGAN KELUARGA'] == "Kepala Keluarga"]
data_didiagnosis_TB_paru=df.loc[df['DI DIAGNOSIS TB PARU'] == "Y"]
data_status_kawin=df.loc[df['STATUS KAWIN'] == "kawin"]
data_jenis_kelamin=df.loc[df['JENIS KELAMIN'] == "perempuan"]
data_didiagnosis_hipertensi=df.loc[df['DI DIAGNOSIS HIPERTENSI'] == "Y"]
data_art_gangguan_jiwa_berat=df.loc[df['ADA ART DI DIAGNOSIS GANGGUAN JIWA BERAT'] == "Y"]
data_asi_eksklusif=df.loc[df['UMUR (BULAN)'] == "7:23"]
data_imunisasi=df.loc[df['UMUR (BULAN)'] == "12:23"]
data_pertumbuhan_balita=df.loc[df['UMUR (BULAN)'] == "2:59"]
#yg filter sudah punya anak belum tau gmn caranya

data_KK=df.DataFrame[data_kepala_keluarga['NAMA KK', 'IKS INTI', 'IKS BESAR', 'JUMLAH ART', 'JUMLAH ART DI WAWANCARA',
                     'JUMLAH ART DEWASA ( >= 15 TAHUN )', 'JUMLAH ART USIA 10 - 54 TAHUN', 'JUMLAH ART USIA 12 - 59 BULAN',
                     'JUMLAH ART USIA 0 - 11 BULAN', 'TERSEDIA SARANA AIR BERSIH', 'JENIS SUMBER AIR TERLINDUNG',
                     'TERSEDIA JAMBAN KELUARGA', 'JENIS JAMBAN SANITER', 'ADA ART DI DIAGNOSIS GANGGUAN JIWA BERAT',
                     'ART MINUM OBAT GANGGUAN JIWA BERAT TERATUR', 'ADA ART DIPASUNG']]

!pip install atoti

!pip install pyngrok

import atoti as tt
from pyngrok import ngrok

port = 9090
ngrok_connection = ngrok.connect(port)

config = tt.config.create_config(url_pattern=ngrok_connection.public_url, port=port)

session = tt.create_session(config=config)

base = session.read_csv("batu_putih.csv",encoding= 'utf-8', sep = '/')
cube = session.create_cube(base)

print(session.url)

base.head()

cube = session.create_cube(base, name="Churn_Data")

cube

