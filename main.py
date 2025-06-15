import pandas as pd
import streamlit as st
import kagglehub

INDIVIDUALS = [
    "Kabir",
    "Sanjit",
    "Nandini"
]


st.title("Age to salary scenario prediction")

with st.container(border=True):
    users = st.multiselect("Users", INDIVIDUALS, default=INDIVIDUALS)

tab1, tab2 = st.tabs(["Kabir", "Dataframe"])


with tab1:
    # Load the CSV data into a DataFrame
    try:
        df_chart = pd.read_csv("salary_data.csv")
    except FileNotFoundError:
        df_chart = pd.DataFrame({
            "Age": [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
            "Salary": [10000, 15000, 25000, 30000, 50000, 60000, 70000, 80000, 90000, 100000, 120000]
        })

    chart = st.line_chart(
        data=df_chart,
        x="Age",
        y="Salary",
        use_container_width=True,
        height=300,
        width=500,
    )

with tab2:
    df = kagglehub.load_dataset("codebreaker619/salary-data-with-age-and-experience", path="salary_data.csv", handle="pandas")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        label="Download Data",
        data=df.to_csv(index=False),
        file_name="salary_data.csv",
        mime="text/csv"
    )

    st.write("Data Source: [KaggleHub](https://www.kaggle.com/datasets/codebreaker619/salary-data-with-age-and-experience/data")


