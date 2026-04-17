import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('model_dropout.pkl')

st.title("🎓 Prediksi Dropout Mahasiswa")
st.write("Isi data mahasiswa untuk memprediksi potensi dropout")

# ===============================
# DICTIONARY KATEGORIKAL
# ===============================

marital_dict = {
    "Single": 1, "Married": 2, "Widower": 3,
    "Divorced": 4, "Facto Union": 5, "Legally Separated": 6
}

app_mode_dict = {
    "1 - General contingent": 1,
    "2 - Ordinance 612/93": 2,
    "5 - Azores special": 5,
    "7 - Other higher courses": 7,
    "10 - Ordinance 854-B/99": 10,
    "15 - International student": 15,
    "16 - Madeira special": 16,
    "17 - 2nd phase": 17,
    "18 - 3rd phase": 18,
    "26 - Different plan": 26,
    "27 - Other institution": 27,
    "39 - Over 23 years": 39,
    "42 - Transfer": 42,
    "43 - Change course": 43,
    "44 - Tech specialization": 44,
    "51 - Change institution": 51,
    "53 - Short cycle": 53,
    "57 - International change": 57
}

course_dict = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (Evening)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing": 9670,
    "Journalism": 9773,
    "Basic Education": 9853,
    "Management (Evening)": 9991
}

attendance_dict = {"Evening": 0, "Daytime": 1}

prev_qual_dict = {
    "Secondary education": 1,
    "Bachelor": 2,
    "Degree": 3,
    "Master": 4,
    "Doctorate": 5,
    "Higher education frequency": 6,
    "12th not completed": 9,
    "11th not completed": 10,
    "Other 11th": 12,
    "10th year": 14,
    "10th not completed": 15,
    "Basic education 3rd cycle": 19,
    "Basic education 2nd cycle": 38,
    "Tech specialization": 39,
    "Degree (1st cycle)": 40,
    "Professional higher tech": 42,
    "Master (2nd cycle)": 43
}

nation_dict = {
    "Portuguese": 1, "German": 2, "Spanish": 6, "Italian": 11,
    "Dutch": 13, "English": 14, "Lithuanian": 17,
    "Angolan": 21, "Cape Verdean": 22, "Guinean": 24,
    "Mozambican": 25, "Santomean": 26, "Turkish": 32,
    "Brazilian": 41, "Romanian": 62, "Moldova": 100,
    "Mexican": 101, "Ukrainian": 103, "Russian": 105,
    "Cuban": 108, "Colombian": 109
}

yesno_dict = {"Tidak": 0, "Ya": 1}
gender_dict = {"Female": 0, "Male": 1}
tuition_dict = {"Menunggak": 0, "Lunas": 1}
scholarship_dict = {"Tidak": 0, "Ya": 1}

# ===============================
# DATA PRIBADI
# ===============================

st.subheader("📌 Data Pribadi")

col1, col2 = st.columns(2)

with col1:
    Marital_status = marital_dict[st.selectbox("Marital Status", marital_dict.keys())]
    Application_mode = app_mode_dict[st.selectbox("Application Mode", app_mode_dict.keys())]
    Application_order = st.slider("Application Order", 0, 9)
    Course = course_dict[st.selectbox("Course", course_dict.keys())]
    Daytime_evening_attendance = attendance_dict[st.selectbox("Class Type", attendance_dict.keys())]
    Previous_qualification = prev_qual_dict[st.selectbox("Previous Qualification", prev_qual_dict.keys())]
    Previous_qualification_grade = st.slider("Previous Qualification Grade", 0.0, 200.0)
    Nacionality = nation_dict[st.selectbox("Nationality", nation_dict.keys())]

with col2:
    Mothers_qualification = st.number_input("Mother Qualification", value=1)
    Fathers_qualification = st.number_input("Father Qualification", value=1)
    Mothers_occupation = st.number_input("Mother Occupation", value=1)
    Fathers_occupation = st.number_input("Father Occupation", value=1)
    Admission_grade = st.slider("Admission Grade", 0.0, 200.0)
    Displaced = yesno_dict[st.selectbox("Displaced", yesno_dict.keys())]
    Educational_special_needs = yesno_dict[st.selectbox("Special Needs", yesno_dict.keys())]
    Debtor = yesno_dict[st.selectbox("Debtor", yesno_dict.keys())]
    Tuition_fees_up_to_date = tuition_dict[st.selectbox("Tuition Fees", tuition_dict.keys())]
    Gender = gender_dict[st.selectbox("Gender", gender_dict.keys())]
    Scholarship_holder = scholarship_dict[st.selectbox("Scholarship", scholarship_dict.keys())]
    Age_at_enrollment = st.number_input("Age", 16, 60)
    International = yesno_dict[st.selectbox("International", yesno_dict.keys())]

# ===============================
# AKADEMIK
# ===============================

st.subheader("📚 Data Akademik")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### Semester 1")
    Curricular_units_1st_sem_credited = st.number_input("CU1 Credited", value=0)
    Curricular_units_1st_sem_enrolled = st.number_input("CU1 Enrolled", value=0)
    Curricular_units_1st_sem_evaluations = st.number_input("CU1 Evaluations", value=0)
    Curricular_units_1st_sem_approved = st.number_input("CU1 Approved", value=0)
    Curricular_units_1st_sem_grade = st.slider("CU1 Grade", 0.0, 20.0)
    Curricular_units_1st_sem_without_evaluations = st.number_input("CU1 Without Eval", value=0)

with col4:
    st.markdown("### Semester 2")
    Curricular_units_2nd_sem_credited = st.number_input("CU2 Credited", value=0)
    Curricular_units_2nd_sem_enrolled = st.number_input("CU2 Enrolled", value=0)
    Curricular_units_2nd_sem_evaluations = st.number_input("CU2 Evaluations", value=0)
    Curricular_units_2nd_sem_approved = st.number_input("CU2 Approved", value=0)
    Curricular_units_2nd_sem_grade = st.slider("CU2 Grade", 0.0, 20.0)
    Curricular_units_2nd_sem_without_evaluations = st.number_input("CU2 Without Eval", value=0)

# ===============================
# EKONOMI
# ===============================

st.subheader("💰 Data Ekonomi")

col5, col6 = st.columns(2)

with col5:
    Unemployment_rate = st.number_input("Unemployment Rate (%)", value=0.0)

with col6:
    Inflation_rate = st.number_input("Inflation Rate (%)", value=0.0)
    GDP = st.number_input("GDP", value=0.0)

# ===============================
# PREDIKSI
# ===============================

st.markdown("---")

if st.button("🔍 Prediksi"):

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
        st.error(f"Berpotensi Dropout (Prob: {prob[1]:.2f})")
    else:
        st.success(f"Tidak Dropout (Prob: {prob[0]:.2f})")