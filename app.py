import streamlit as st
from converter import convert

st.set_page_config(page_title="Temperature Converter", page_icon="🌡", layout="centered")

st.title("🌡 Smart Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin instantly.")

value = st.number_input("Enter temperature value", format="%.2f")

unit = st.selectbox(
    "Choose input unit",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

if st.button("Convert Temperature"):

    result = convert(value, unit)

    if result:
        st.subheader("Converted Values")

        for key, val in result.items():
            st.success(f"{key}: {val:.2f}")

    else:
        st.error("Invalid unit selected")
