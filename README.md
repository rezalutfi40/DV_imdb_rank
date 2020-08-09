## Web Scraping and visualizatin imdb by Reza Lutfi Ismail 

# Introduction
projek ini adalah sebuah projek penarikan data pada URL: https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31, 
yang berisikan daftar film populer pada tahun 2019. pada proses pengerjaannya, saya menggunakan VS code

# Dependencies
menggunakan modul beutifulsoup4 yang sudah di install pada pip install beautifulsoup4. dan jug amenggunakan library: 

- pandas
- matplotlibs

# Scraping
menarik data pada URL dengan memilih area pada HTML. lalu disajikan dengan menggunakan beautifulsoup. output dari proses ini adalah 
berupa list yang nantinya akan diproses lebih lanjut oleh pandas

# Data Wranglig
memproses data yang sebelumnya berupa list, menjadi dataframe dengan tipe data yang sesuai dengan menggunakan pandas. dilakukan juga 
sorting untuk menentukan film dengan rating tertinggi. output dari proses ini adalah data yang bersih dan siap untuk divisualisasikan

# Data Visualization
tahap ini yaitu menyajikan datframe kedalam bentuk plot (bar) agar data lebih menarik dan mudah untuk dipahami

## Conclusion
pada projek ini, dapat kita ketahui bahwa pada URL: https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31, 7 film 
dengan rating tertinggi secara urut adalah: Chernobyl, The Boys, The Mandalorian, Gisaengchung, Joker, What We Do in the Shadows dan 
The Morning Show

