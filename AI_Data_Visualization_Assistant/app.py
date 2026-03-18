import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Data Visualization Assistant")

st.write("Upload a CSV file to visualize data")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    numeric_columns = df.select_dtypes(include=['int64','float64']).columns

    column = st.selectbox("Select Column", numeric_columns)

    chart = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Histogram"])

    if st.button("Generate Visualization"):
        fig, ax = plt.subplots()

        if chart == "Bar Chart":
            df[column].value_counts().plot(kind='bar', ax=ax)

        elif chart == "Line Chart":
            df[column].plot(ax=ax)

        elif chart == "Histogram":
            df[column].plot(kind='hist', ax=ax)

        st.pyplot(fig)

    st.subheader("Basic Insights")
    st.write("Mean:", df[column].mean())
    st.write("Max:", df[column].max())
    st.write("Min:", df[column].min())