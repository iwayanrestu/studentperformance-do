# Proyek Akhir: Student Performance & Dropout Risk Monitoring

## Business Understanding

### Background

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun demikian, terdapat sejumlah mahasiswa yang tidak menyelesaikan pendidikannya (dropout).

Tingginya angka dropout menjadi permasalahan serius karena:

- Mengurangi tingkat kelulusan institusi
- Berdampak pada reputasi akademik
- Menunjukkan adanya ketidakefisienan dalam proses pendidikan

Oleh karena itu, pihak institusi ingin mendeteksi mahasiswa yang berpotensi dropout sedini mungkin, sehingga dapat diberikan intervensi atau bimbingan khusus.

---

## Permasalahan Bisnis

Permasalahan utama yang dihadapi oleh Jaya Jaya Institut adalah:

1. Tingginya angka dropout mahasiswa
2. Sulitnya mengidentifikasi mahasiswa berisiko sejak dini
3. Kurangnya insight terkait faktor penyebab dropout
4. Tidak adanya sistem monitoring performa mahasiswa secara terpusat
5. Keterlambatan dalam memberikan intervensi kepada mahasiswa bermasalah

---

## Cakupan Proyek

Proyek ini mencakup beberapa hal utama:

### 1. Data Analysis (EDA)

- Menganalisis faktor-faktor yang mempengaruhi dropout
- Mengidentifikasi pola dari performa mahasiswa

### 2. Machine Learning

- Membangun model prediksi dropout
- Mengklasifikasikan mahasiswa menjadi:
  - Dropout
  - Tidak dropout

### 3. Business Dashboard

- Membuat dashboard interaktif
- Memvisualisasikan performa mahasiswa
- Monitoring kondisi mahasiswa secara real-time

### 4. Deployment Sederhana

- Membuat prototype aplikasi prediksi menggunakan Streamlit

---

## Persiapan

### Sumber Data

Dataset: [Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
Berisi informasi:

- Data demografi
- Data akademik semester 1 dan 2
- Data finansial
- Status mahasiswa (target)

---

## Setup Environment (Virtual Environment)

### 1. Membuat Virtual Environment

```bash
python -m venv venv
```

### 2. Mengaktifkan Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

## Install Library

Jika sudah tersedia file `requirements.txt`, jalankan:

```bash
pip install -r requirements.txt
```

Contoh isi `requirements.txt`:

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

---

## Menjalankan Proyek

### 1. Menjalankan Notebook (Opsional)

```bash
jupyter notebook
```

### 2. Menjalankan Aplikasi Machine Learning

```bash
streamlit run app.py
```

Kemudian buka di browser:

```
http://localhost:8501
```

### 3. Akses Aplikasi (Online)

Aplikasi juga dapat diakses secara online melalui link berikut:

```
https://studentperformance-do-satvjug2doldm4kappzvtua.streamlit.app/
```

---

## Business Dashboard

Dashboard yang dibuat berjudul:

Student Performance & Dropout Risk Monitoring

### Filter yang digunakan:

- Gender
- Scholarship
- Course
- Tuition Status

---

### Visualisasi yang ditampilkan:

1. Jumlah Mahasiswa Berdasarkan Status
   - Graduate
   - Dropout

2. Dropout Rate (%)
   - Menunjukkan persentase mahasiswa dropout sekitar 32%

3. Rata-rata Nilai Akademik
   - Perbandingan Semester 1 dan Semester 2
   - Berdasarkan status mahasiswa

4. Jumlah Unit yang Disetujui
   - Semester 1 dan Semester 2
   - Indikator performa akademik

5. Status Pembayaran (Tuition)
   - Perbandingan antara mahasiswa dropout dan status pembayaran

6. Status Beasiswa
   - Pengaruh beasiswa terhadap dropout

7. Distribusi Dropout per Jurusan
   - Menunjukkan jurusan dengan tingkat dropout tinggi

### Cara Mengakses:

Buka link dashboard berikut di browser:

```
https://datastudio.google.com/reporting/677133ad-cb96-4309-930d-372a565a36cf
```

Setelah dashboard terbuka, gunakan fitur filter yang tersedia untuk melakukan eksplorasi data:

- Gender
- Scholarship
- Course
- Tuition Status

Analisis visualisasi yang ditampilkan, seperti:

- Distribusi status mahasiswa (Graduate, Dropout)
- Dropout rate (%)
- Performa akademik semester 1 dan 2
- Jumlah mata kuliah yang disetujui
- Status pembayaran dan beasiswa
- Distribusi dropout per jurusan

---

## Insight (Berdasarkan EDA)

Berdasarkan analisis data:

1. Performa Akademik
   Mahasiswa dropout memiliki jumlah mata kuliah lulus yang sangat rendah, bahkan banyak yang bernilai 0 terutama di semester awal. Ini menjadi indikator paling kuat.

2. Status Pembayaran
   Mahasiswa dengan tunggakan biaya kuliah memiliki kecenderungan dropout yang jauh lebih tinggi.

3. Beasiswa
   Mahasiswa penerima beasiswa memiliki tingkat kelulusan yang jauh lebih tinggi dibandingkan yang tidak.

4. Usia
   Mahasiswa dengan usia lebih tua saat mendaftar memiliki risiko dropout lebih tinggi.

5. Gender
   Mahasiswa laki-laki menunjukkan kecenderungan dropout lebih tinggi dibandingkan perempuan.

---

## Hasil Model Machine Learning

Model yang digunakan:
Logistic Regression dengan Pipeline dan StandardScaler

### Hasil Evaluasi:

- Accuracy: sekitar 0.91
- F1 Score: sekitar 0.90
- Recall untuk dropout: sekitar 0.84

### Kesimpulan Model:

Model mampu mengidentifikasi mahasiswa berisiko dropout dengan cukup baik dan dapat digunakan sebagai sistem deteksi awal.

---

## Conclusion

### 1. Kesimpulan Berdasarkan Analisis Data (EDA & Dashboard)

Berdasarkan hasil eksplorasi data (EDA) dan visualisasi pada dashboard, ditemukan beberapa faktor utama yang berkaitan dengan terjadinya dropout mahasiswa:

- **Performa akademik semester awal** merupakan faktor paling dominan. Mahasiswa dengan jumlah mata kuliah yang disetujui (approved) rendah, terutama di semester 1 dan 2, memiliki kecenderungan tinggi untuk dropout. Bahkan banyak mahasiswa dropout yang tidak meluluskan satu pun mata kuliah.

- **Nilai akademik (grade)** yang rendah juga berkontribusi signifikan terhadap risiko dropout, baik pada semester pertama maupun kedua.

- **Status pembayaran biaya kuliah (tuition fees)** menunjukkan pengaruh yang kuat. Mahasiswa yang memiliki tunggakan pembayaran cenderung lebih banyak mengalami dropout dibandingkan yang pembayarannya lancar.

- **Status beasiswa** memiliki dampak positif terhadap kelulusan. Mahasiswa penerima beasiswa cenderung memiliki tingkat dropout yang lebih rendah.

- **Usia saat pendaftaran** menunjukkan bahwa mahasiswa dengan usia lebih tinggi memiliki risiko dropout yang lebih besar.

- **Gender** juga menunjukkan pola tertentu, di mana mahasiswa laki-laki memiliki kecenderungan dropout lebih tinggi dibandingkan perempuan.

Secara keseluruhan, faktor akademik dan finansial menjadi indikator utama dalam menentukan risiko dropout mahasiswa.

---

### 2. Kesimpulan Berdasarkan Model Machine Learning

Model machine learning yang digunakan adalah **Logistic Regression** dengan pipeline yang mencakup StandardScaler.

Hasil evaluasi model menunjukkan performa sebagai berikut:

- **Accuracy**: sekitar 0.91
- **F1 Score**: sekitar 0.90
- **Recall (Dropout)**: sekitar 0.84

Hasil ini menunjukkan bahwa model memiliki kemampuan yang cukup baik dalam mengklasifikasikan mahasiswa yang berpotensi dropout maupun tidak.

Berdasarkan karakteristik model Logistic Regression, fitur-fitur yang paling berpengaruh terhadap prediksi (berdasarkan koefisien model) meliputi:

- Jumlah mata kuliah yang disetujui pada semester 1 dan 2
- Nilai rata-rata semester 1 dan 2
- Status pembayaran biaya kuliah
- Status beasiswa
- Admission grade

---

## Implikasi Bisnis

Dengan adanya sistem ini, institusi dapat:

- Mengidentifikasi mahasiswa berisiko lebih cepat
- Mengurangi angka dropout
- Meningkatkan tingkat kelulusan
- Mengambil keputusan berbasis data

---

## Rekomendasi Action Items

1. Membuat sistem early warning berbasis performa akademik semester 1
2. Menyediakan program bimbingan khusus bagi mahasiswa berisiko
3. Memberikan bantuan finansial atau skema pembayaran fleksibel
4. Melakukan monitoring rutin melalui dashboard
5. Memperluas program beasiswa bagi mahasiswa yang membutuhkan
