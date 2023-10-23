# app.py
import streamlit as st
from pypmml import Model

# Load the PMML model
model = Model.fromFile('revenue_prediction_model.pmml')

# prediction = model.predict([886, 616, 125, 295])
# print(prediction)

# Judul Aplikasi
st.title('Aplikasi Prediksi')

# Input 1
input1 = int(st.number_input('Qty Tire Micheline yang akan di Billing dalam 1 bulan', value=0))

# Input 2
input2 = int(st.number_input('Qty Tire Micheline Earthmover yang akan di Billing dalam 1 bulan', value=0))

# Input 3
input3 = int(st.number_input('Qty PO Micheline yang akan dihitung dalam 1 bulan', value=0))

# Input 4
input4 = float(st.number_input('Target leadtime (satuan hari) dari Factory ke CP', value=0.00, format="%.3f"))

# Prediksi ketika tombol ditekan
if st.button('Prediksi'):
    # Lakukan prediksi dengan model
    prediction = model.predict([input1, input2, input3, input4])
    prediction_str = str(prediction)
    st.write('Hasil Prediksi: ', prediction_str)
