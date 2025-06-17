import pandas as pd
import streamlit as st
import kagglehub
import altair as alt

INDIVIDUALS = [
    "Kabir",
    "Sanjit",
    "Nandini"
]


class GetUserSynthesis():
    def __init__(self, users):
        self.user = users

    def get_users(self):
        if self.user not in INDIVIDUALS:
            raise ValueError(f"User {self.user} is not in the list of individuals: {INDIVIDUALS}")
        if self.user == "Kabir":
            return "Kabir created an application that solved a real-world issue at the age of 22. " \
            "His profits soared for the first few years, but then dipped down suddenly as he lost some of his user base." \
            "A new sofware update more geared towards the user experience of the application lead him to a steady and marginally " \
            "increasing income for the next few years"
        elif self.user == "Sanjit":
            return "Sanjit created an application that solved a real-world issue. His profits soared from the age of 22 " \
            "to the age of 23, then suddenly decreased. Sanjit got investors to invest in his application, and his income " \
            "started to steadily increase again."
        elif self.user == "Nandini":
            return "Nandini created an application that solved a real-world problem, and profits soared. Then, sales started to go " \
            "down as her user base lost interest, so she sold her app for a yearly income to a company, and her profits marginally " \
            "increased over time."


    






st.title("Age to Salary Scenario Prediction")

with st.container(border=True):
    users = st.multiselect("Users", INDIVIDUALS, default=INDIVIDUALS)

tab1, tab2 = st.tabs(["Chart", "Dataframe"])


kagglehub.dataset_download("codebreaker619/salary-data-with-age-and-experience")

try:
    df = pd.read_csv("salary_data.csv")
    all_users = df["User"].unique().tolist()
except FileNotFoundError:
    df = pd.DataFrame({
        "User": ["Kabir", "Sanjit", "Nandini"],
        "Age": [21, 22, 23],
        "Salary": [39343, 46205, 37731]
    })

df["Age"] = df["Age"].round().astype(int)


filtered_df = df[df["User"].isin(users)]

with tab1:
    if filtered_df.empty:
        st.info("No data to display. Please select at least one user.")
    else:
        chart = alt.Chart(filtered_df).mark_line(point=True).encode(
            x=alt.X('Age:Q', title='Age'),
            y=alt.Y('Salary:Q', title='Salary'),
            color=alt.Color('User:N', title='User'),
            tooltip=['User', 'Age', 'Salary']
        ).properties(
            width='container',
            height=400,
            title="Age vs Salary by User"
        )
        st.altair_chart(chart, use_container_width=True)

        for user in users:
            if user not in filtered_df['User'].unique():
                st.warning(f"No data available for {user}, but here’s the synthesis anyway.")

            user_synthesis = GetUserSynthesis(users=user)

            st.markdown(
                f"### User Synthesis for {user}:\n{user_synthesis.get_users()}"
            )




with tab2:
    st.dataframe(filtered_df, use_container_width=True)

    st.download_button(
        label="Download Filtered Data",
        data=filtered_df.to_csv(index=False),
        file_name="filtered_salary_data.csv",
        mime="text/csv"
    )

    st.write("Data Source: [KaggleHub](https://www.kaggle.com/datasets/codebreaker619/salary-data-with-age-and-experience/data)")
