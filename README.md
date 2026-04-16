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

Dataset: Student Performance Dataset
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
   - Enrolled

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

- Accuracy: sekitar 0.87
- F1 Score: sekitar 0.86
- Recall untuk dropout: sekitar 0.72

### Kesimpulan Model:

Model mampu mengidentifikasi mahasiswa berisiko dropout dengan cukup baik dan dapat digunakan sebagai sistem deteksi awal.

---

## Conclusion

Berdasarkan hasil analisis dan pemodelan:

- Faktor paling dominan adalah performa akademik pada semester awal
- Faktor finansial seperti pembayaran biaya kuliah juga sangat berpengaruh
- Banyak mahasiswa yang dropout sudah menunjukkan tanda sejak semester pertama
- Diperlukan sistem monitoring dan deteksi dini untuk menekan angka dropout

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
