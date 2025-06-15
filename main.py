import pandas as pd
import streamlit as st
import kagglehub
import altair as alt

INDIVIDUALS = [
    "Kabir",
    "Sanjit",
    "Nandini"
]

st.title("Age to Salary Scenario Prediction")

with st.container(border=True):
    users = st.multiselect("Users", INDIVIDUALS, default=INDIVIDUALS)

tab1, tab2 = st.tabs(["Chart", "Dataframe"])


try:
    df = pd.read_csv("salary_data.csv")
except FileNotFoundError:
    df = pd.DataFrame({
        "User": ["Kabir", "Sanjit", "Nandini"],
        "Age": [21, 22, 23],
        "Salary": [39343, 46205, 37731]
    })


df["Age"] = df["Age"].round().astype(int)


filtered_df = df[df["User"].isin(users)]

with tab1:
    st.line_chart(
        data=filtered_df,
        x="Age",
        y="Salary",
        use_container_width=True,
        height=300
    )

with tab2:
    kagglehub.dataset_download("codebreaker619/salary-data-with-age-and-experience")
    st.dataframe(filtered_df, use_container_width=True)

    st.download_button(
        label="Download Filtered Data",
        data=filtered_df.to_csv(index=False),
        file_name="filtered_salary_data.csv",
        mime="text/csv"
    )

    st.write("Data Source: [KaggleHub](https://www.kaggle.com/datasets/codebreaker619/salary-data-with-age-and-experience/data)")
