import streamlit as st
import numpy as np
import joblib

model = joblib.load('model_dropout.pkl')

st.title("🎓 Prediksi Dropout Mahasiswa")
st.write("Masukkan data mahasiswa sesuai keterangan di setiap input")

# ===============================
# DATA PRIBADI
# ===============================

Marital_status = st.selectbox(
    "Marital Status",
    [1,2,3,4,5,6],
    help="1=Single, 2=Married, 3=Widower, 4=Divorced, 5=Facto Union, 6=Legally Separated"
)

Application_mode = st.number_input(
    "Application Mode",
    help="Contoh: 1,2,5,7,15... (kode jalur masuk kampus)"
)

Application_order = st.slider(
    "Application Order",
    0, 9,
    help="0 = pilihan pertama, 9 = pilihan terakhir"
)

Course = st.number_input(
    "Course Code",
    help="Contoh: 9119 = Informatics Engineering"
)

Daytime_evening_attendance = st.selectbox(
    "Daytime / Evening",
    [0,1],
    help="1 = Daytime, 0 = Evening"
)

Previous_qualification = st.number_input(
    "Previous Qualification",
    help="Contoh: 1=Secondary, 2=Bachelor, 3=Degree, dst"
)

Previous_qualification_grade = st.slider(
    "Previous Qualification Grade",
    0.0, 200.0,
    help="Nilai pendidikan sebelumnya (0–200)"
)

Nacionality = st.number_input(
    "Nationality",
    help="Contoh: 1=Portuguese, 41=Brazilian"
)

Mothers_qualification = st.number_input(
    "Mother Qualification",
    help="Kode pendidikan ibu (angka kategori)"
)

Fathers_qualification = st.number_input(
    "Father Qualification",
    help="Kode pendidikan ayah (angka kategori)"
)

Mothers_occupation = st.number_input(
    "Mother Occupation",
    help="Kode pekerjaan ibu (angka kategori)"
)

Fathers_occupation = st.number_input(
    "Father Occupation",
    help="Kode pekerjaan ayah (angka kategori)"
)

Admission_grade = st.slider(
    "Admission Grade",
    0.0, 200.0,
    help="Nilai masuk kampus (0–200)"
)

Displaced = st.selectbox(
    "Displaced",
    [0,1],
    help="1 = Ya, 0 = Tidak"
)

Educational_special_needs = st.selectbox(
    "Educational Special Needs",
    [0,1],
    help="1 = Ya, 0 = Tidak"
)

Debtor = st.selectbox(
    "Debtor",
    [0,1],
    help="1 = Memiliki hutang, 0 = Tidak"
)

Tuition_fees_up_to_date = st.selectbox(
    "Tuition Fees Up To Date",
    [0,1],
    help="1 = Lunas, 0 = Menunggak"
)

Gender = st.selectbox(
    "Gender",
    [0,1],
    help="1 = Male, 0 = Female"
)

Scholarship_holder = st.selectbox(
    "Scholarship",
    [0,1],
    help="1 = Ya, 0 = Tidak"
)

Age_at_enrollment = st.number_input(
    "Age",
    16, 60,
    help="Umur saat masuk kuliah"
)

International = st.selectbox(
    "International Student",
    [0,1],
    help="1 = Ya, 0 = Tidak"
)

# ===============================
# AKADEMIK
# ===============================

st.subheader("📚 Data Akademik Semester 1")

Curricular_units_1st_sem_credited = st.number_input(
    "CU1 Credited",
    help="Jumlah mata kuliah yang diakui"
)

Curricular_units_1st_sem_enrolled = st.number_input(
    "CU1 Enrolled",
    help="Jumlah mata kuliah yang diambil"
)

Curricular_units_1st_sem_evaluations = st.number_input(
    "CU1 Evaluations",
    help="Jumlah evaluasi/ujian"
)

Curricular_units_1st_sem_approved = st.number_input(
    "CU1 Approved",
    help="Jumlah mata kuliah yang lulus"
)

Curricular_units_1st_sem_grade = st.slider(
    "CU1 Grade",
    0.0, 20.0,
    help="Rata-rata nilai semester 1 (0–20)"
)

Curricular_units_1st_sem_without_evaluations = st.number_input(
    "CU1 Without Evaluations",
    help="Jumlah mata kuliah tanpa evaluasi"
)

st.subheader("📚 Data Akademik Semester 2")

Curricular_units_2nd_sem_credited = st.number_input(
    "CU2 Credited",
    help="Jumlah mata kuliah yang diakui"
)

Curricular_units_2nd_sem_enrolled = st.number_input(
    "CU2 Enrolled",
    help="Jumlah mata kuliah yang diambil"
)

Curricular_units_2nd_sem_evaluations = st.number_input(
    "CU2 Evaluations",
    help="Jumlah evaluasi/ujian"
)

Curricular_units_2nd_sem_approved = st.number_input(
    "CU2 Approved",
    help="Jumlah mata kuliah yang lulus"
)

Curricular_units_2nd_sem_grade = st.slider(
    "CU2 Grade",
    0.0, 20.0,
    help="Rata-rata nilai semester 2 (0–20)"
)

Curricular_units_2nd_sem_without_evaluations = st.number_input(
    "CU2 Without Evaluations",
    help="Jumlah mata kuliah tanpa evaluasi"
)

# ===============================
# EKONOMI
# ===============================

Unemployment_rate = st.number_input(
    "Unemployment Rate",
    help="Tingkat pengangguran (%) contoh: 11.5"
)

Inflation_rate = st.number_input(
    "Inflation Rate",
    help="Tingkat inflasi (%) contoh: 1.2"
)

GDP = st.number_input(
    "GDP",
    help="Nilai GDP (bisa negatif atau positif)"
)

# ===============================
# PREDIKSI
# ===============================

if st.button("Prediksi"):

    input_data = np.array([[ 
        Marital_status, Application_mode, Application_order, Course,
        Daytime_evening_attendance, Previous_qualification,
        Previous_qualification_grade, Nacionality,
        Mothers_qualification, Fathers_qualification,
        Mothers_occupation, Fathers_occupation,
        Admission_grade, Displaced, Educational_special_needs,
        Debtor, Tuition_fees_up_to_date, Gender,
        Scholarship_holder, Age_at_enrollment, International,
        Curricular_units_1st_sem_credited,
        Curricular_units_1st_sem_enrolled,
        Curricular_units_1st_sem_evaluations,
        Curricular_units_1st_sem_approved,
        Curricular_units_1st_sem_grade,
        Curricular_units_1st_sem_without_evaluations,
        Curricular_units_2nd_sem_credited,
        Curricular_units_2nd_sem_enrolled,
        Curricular_units_2nd_sem_evaluations,
        Curricular_units_2nd_sem_approved,
        Curricular_units_2nd_sem_grade,
        Curricular_units_2nd_sem_without_evaluations,
        Unemployment_rate, Inflation_rate, GDP
    ]])

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error(f"⚠️ Berpotensi Dropout (Prob: {prob[1]:.2f})")
    else:
        st.success(f"✅ Tidak Dropout (Prob: {prob[0]:.2f})")
        