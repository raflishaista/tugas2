Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Membuat sebuah proyek Django baru.
Saya membuat suatu virtual environment, dan menyiapkan dependencies-dependencies yang dibutuhkan.
    Membuat aplikasi dengan nama main
Dengan membuat aplikasi baru bernama main dengan command seperti startapp, dan dengan menambahkan konfigurasi MVT, serta mendaftarkan aplikasi ke proyek
    Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Di dalam direktori proyek, urls.py dibuat, dan didalamnya ditambahkan kode untuk berbagai fungsi, seperti mengatur rute URL.
    Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
Membuat suatu file bernama models.py, dan mengisinya dengan nama class item serta atribut-atribut name,amount,dan description didalamnya, serta mengassign field yang sesuai.
    Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Sesuai dengan variabel di models, setiap variabel diberi value yang sesuai dengan field
    Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Di dalam direktori main, urls.py dibuat, dan didalamnya ditambahkan kode untuk berbagai fungsi, seperti mendefinsikan URL.
    Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Sebelumnya, saya push dahulu proyek kepada github, kemudian saya hubungkan di Adaptable. Untuk deployment, saya memilih Python App Template, PostgreSQL, dan Python 3.10. Kemudian, ketika sudah sukses dideploy dan link sudah diberikan, link tersebut memerlukan /main di akhir url tersebut, untuk mengakses app main ini.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

urls.py akan memajukan request pada view berupa views.py yang sesuai, kemudian view akan menerima web request tersebut dan memberikan web response kepada client. views.py dapat menulis atau membaca data ke/dari penyimpanan data dari aplikasi, yaitu models.py. Berkas html, atau template merupakan bagian yang akan dipajang kepada client, yang berupa web response yang diberikan views.py.

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Disini, virtual environment digunakan untuk memisahkan dependecies yang digunakan dalam pembuatan proyek ini, yang ada pada requirements.txt, dengan versi lain yang mungkin ada didalam komputer. Ini bermanfaat jika ada proyek lain yang membutuhkan versi lain dari dependencies dari atau dependency yang berbeda dari virtual environment sendiri sehingga tidak bertabrakan dengan virtual environment. Aplikasi web berbasis Django masih dapat dibuat tanpa virtual environment.

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC, MVT, dan MVVM adalah berbagai jenis dari design pattern, suatu solusi desain software yang dapat digunakan beberapa kali dan dapat digunakan ulang, sesuai masalah desain yang dihadapi dalam berbagai situasi. MVC adalah framework yang terdiri dari model, view, dan controller. MVT adalah framework yang terdiri dari model view, dan template. MVCC adalah framework yang terdiri dari model, view, dan viewmodel. Controller berfungsi dalam mengontrol interaksi antara model dan view, template berfungsi sebagai user interface, dan viewmodel memiliki binder yang dapat mengotomasi komunikasi antara view dan properti view di viewmodel, sehingga view mengikat propertinya pada viewmodel untuk mendapatkan update-update.