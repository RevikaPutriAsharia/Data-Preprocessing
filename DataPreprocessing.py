#Nama : Revika Putri Asharia
#NPM : F1A022016
#Tugas 1 Data Mining

#1. Memuat Data
#a. Import library yaitu menggunakan library pandas
import pandas as pd

#b. Memuat dataset dari file CSV ke dalam DataFrame
df = pd.read_csv('C:/Users/UseRj_/Documents/movie_sample_dataset.csv')

#2. Memeriksa Data
#a. Tampilkan beberapa baris pertama dari dataset untuk memahami struktur data
print("Menampilkan Beberapa Baris Pertama dari Dataset untuk Memahami Struktur Data")
print(df.head())

#b. Periksa informasi umum tentang dataset termasuk tipe data dan nilai yang hilang
#Import library yaitu menggunakan library numpy
import numpy as np
# Mengganti "Nan" dengan " "
df['director_name'] = df['director_name'].replace(['Nan', 'Null'], '', regex=True)

#Memeriksa jumlah missing values di setiap kolom
print("Menampilkan Jumlah Missing Values di Setiap Kolom")
print(df.isnull().sum())

#3. Membersihkan Data
#Hapus baris yang memiliki nilai Nan di kolom penting 
#a. Menghapus baris dengan missing values pada kolom "gross"
df_cleaned1 = df.dropna(subset=["gross"], axis=0, inplace=True)
# Reset index setelah menghapus baris
df.reset_index(drop=True, inplace=True)

#b. Menghapus baris dengan missing values pada kolom "budget"
df_cleaned2 = df.dropna(subset=["budget"], axis=0, inplace=True)
#Reset index setelah menghapus baris
df.reset_index(drop=True, inplace=True)

#c. Atasi nilai yang tidak konsisten atau kesalahan penulisan di kolom seperti perbedaan antara "Color" dan "color" serta "shane black" dan "SHANE BLACK"
#Mengatasi perbedaan antara "Color" dan "color" atau inkonsistensi serupa pada kolom
#Misalnya, kita akan mengubah nilai dalam kolom "color" menjadi huruf kecil semua
if 'color' in df.columns:
    df['color'] = df['color'].str.lower()  # Ubah semua nilai di kolom "color" menjadi huruf kecil
print(df.head())

# Kemudian, mengubah nilai dalam kolom "shane black" menjadi huruf "SHANE BLACK"
if 'country' in df.columns:
    df['country'] = df['country'].str.upper()  # Ubah semua nilai di kolom "shane black" menjadi "SHANE BLACK"
print(df.head())

#d. Ubah atau hapus nilai-nilai yang tidak standar seperti nilai negatif atau "NaN"
#Mengubah nilai negatif pada kolom 'duration' dan 'imdb_score'
#Mengganti nilai negatif dengan NaN
df['duration'] = df['duration'].apply(lambda x: x if x >= 0 else np.nan)
df['imdb_score'] = df['imdb_score'].apply(lambda x: x if x >= 0 else np.nan)

#Mengganti dengan frekuensi pada kolom 'color', 'director name', dan 'genres', duration', dan 'imdb_score'
for column in ['color', 'director_name', 'genres', 'duration', 'imdb_score']:
    #Menentukan nilai yang paling sering muncul (mode)
    mode_value = df[column].mode()[0]
    #Mengganti nilai N/A dengan nilai yang paling sering muncul
    df[column].fillna(mode_value, inplace=True)
    mode_value = df['director_name'].mode()[0]  #Mendapatkan nilai yang paling sering muncul
    df['director_name'].replace('', mode_value, inplace=True)  #Mengganti string kosong dengan mode
#Menampilkan beberapa baris pertama setelah perubahan
print("Data setelah mengubah nilai negatif dan mengganti NaN:")
print(df.head())

#4. Transformasi Data
#a. Ubah tipe data kolom menjadi tipe data yang sesuai (misalnya, konversi genres dari onject ke string) agar bisa dilakukan pemisahan genre yang tergabung dalam satu kolom menjadi beberapa kolom
print(df.dtypes)
df['genres'] = df['genres'].astype(str)
print("Konversi Genres dari Onject ke String")
print(df['genres'])

#Tidak ada yang diubah karena tipe data sudah sesuai Variabel numerik (int atau float) dan variabel kategorik (string atau object)
#b. Normalisasi Teks untuk Memastikan Konsistensi (misalnya mengubah teks menjadi huruf kecil)
#Melakukan normalisasi teks untuk kolom 'color', 'director_name', 'genres', 'movie_title','language', 'country', dan 'actors'
columns_to_normalize = ['color', 'director_name', 'genres', 'movie_title', 'language', 'country', 'actors']
for column in columns_to_normalize:
    df[column] = df[column].str.lower()  # Mengubah teks menjadi huruf kecil
    df[column] = df[column].str.strip()  # Menghapus spasi di awal dan akhir teks
# Menampilkan beberapa baris pertama setelah normalisasi
print("Data setelah Normalisasi:")
print(df.head())
    
#5. Penyimpanan Data
df.to_csv('C:/Users/UseRj_/Documents/movie_dataset_cleaned.csv', index=False)

