import pandas as pd
import streamlit as st
import kagglehub

r1col1, r1col2, r1col3 = st.columns([1, 2, 1])

with r1col1:
    st.title("Age to salary scenario prediction")

st.divider()

tab1, tab2 = st.tabs(["Kabir", "Sanjit", "Nandini"])


with tab1:
    chart = st.line_chart(data="salary_data.csv", 
                x="Age",
                y="Salary",
                use_container_width=True,
                height=300,
                width=500,
                )

    chart.add_rows(
        pd.DataFrame({
            "Age": [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
            "Salary": [10000, 15000, 25000, 30000, 50000, 60000, 70000, 80000, 90000, 100000, 120000]
        })
    )


