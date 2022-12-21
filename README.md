# Praktikum-2-Komnum

## Praktikum membuat program Integrasi Romberg
Nama Kelompok :
  1. Clarissa Luna Maheswari (5025211003)
  2. Rule Lulu Damara (5025211050)
  3. Ghifari Maaliki Syafa Syuhada (5025211158)
  
## Penjelasan
Ekstrapolasi adalah sebuah perkiraan yang jangkauannya melampaui yang diamati, dari sebuah nilai yang dihasilkan oleh sebuah variabel dengan menggunakan basis hubungannya dengan variabel lainnya. Ekstrapolasi hampir sama dengan interpolasi dimana akan menghasilkan sebuah perkiraan dari observasi, akan tetapi perkiraan ekstrapolasi akan cenderung lebih tidak sesuai dan bisa jadi menghasilkan perkiraan yang jauh dari aslinya.
###### Ekstrapolasi Richardson
Ekstrapolasi Richardson adalah sebuah metode yang digunakan untuk meningkatkan tingkat konvergensi dari perkiraan suatu nilai. Misalkan kita ingin mencari sebuah perkiraan dari nilai asli A* yaitu A(h) dimana A merupakan fungsi sebuah nilai. Untuk mendapatkan A* kita bisa melakukan ekstrapolasi dengan mencari limit h mendekati 0.
###### Integrasi Romberg
Integrasi Romberg adalah salah satu metode ekstrapolasi yang merupakan turunan dari ekstrapolasi Richardson. Caranya adalah dengan menerapkan Ekstrapolasi Richardson kepada aturan trapesium. Hasilnya merupakan sebuah array segitiga. Metode ini mirip dengan metode Newton-Cotes, dimana metode ini mengevaluasi integran pada interval yang sama. Metode ini dapat digunakan untuk mengevaluasi integran dengan interval yang berbeda, akan tetapi metode-metode lain bekerja lebih baik untuk menghasilkan perkiraan yang akurat
