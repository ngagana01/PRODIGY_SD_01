import streamlit as st
import pandas as pd
from converter import convert

st.set_page_config(page_title="Temperature Converter", page_icon="🌡", layout="centered")

st.title("🌡 Smart Temperature Converter")
st.caption("Convert temperatures instantly + track history + download results")

# ---------------- SESSION HISTORY ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- INPUT ----------------
value = st.number_input("Enter temperature value", format="%.2f")

unit = st.selectbox(
    "Choose input unit",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

# ---------------- CONVERT BUTTON ----------------
if st.button("Convert Temperature"):
    result = convert(value, unit)

    if result:
        st.subheader("Converted Values")

        row = {"Input": f"{value} {unit}"}

        for key, val in result.items():
            st.success(f"{key}: {val:.2f}")
            row[key] = round(val, 2)

        # Save to history
        st.session_state.history.append(row)

    else:
        st.error("Invalid unit selected")

# ---------------- HISTORY TABLE ----------------
st.divider()
st.subheader("📜 Conversion History")

if st.session_state.history:

    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)

    # DOWNLOAD BUTTON
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download History as CSV",
        data=csv,
        file_name="temperature_history.csv",
        mime="text/csv"
    )

    # CLEAR HISTORY
    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

else:
    st.info("No conversions yet.")

# ---------------- EXTRA FEATURES ----------------
st.divider()
st.markdown("### ⚙ Extra Tools")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Conversions", len(st.session_state.history))

with col2:
    if st.session_state.history:
        last = st.session_state.history[-1]["Input"]
        st.metric("Last Input", last)
