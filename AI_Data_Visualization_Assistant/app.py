import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AI Data Visualization Assistant", layout="wide")

st.title("📊 AI Data Visualization Assistant")
st.write("Upload a CSV file and explore your data visually")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show dataset
    st.subheader("📂 Dataset Preview")
    st.dataframe(df)

    # Dataset info
    st.subheader("📈 Dataset Summary")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Sidebar controls
    st.sidebar.header("⚙️ Options")

    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Histogram", "Pie Chart", "Box Plot", "Correlation Heatmap"]
    )

    if len(numeric_cols) > 0:
        column = st.sidebar.selectbox("Select Numeric Column", numeric_cols)

    # Charts
    st.subheader("📊 Visualization")

    if chart_type == "Bar Chart":
        fig, ax = plt.subplots()
        df[column].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Line Chart":
        fig, ax = plt.subplots()
        df[column].plot(ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        df[column].plot(kind='hist', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots()
        df[column].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Box Plot":
        fig, ax = plt.subplots()
        sns.boxplot(y=df[column], ax=ax)
        st.pyplot(fig)

    elif chart_type == "Correlation Heatmap":
        fig, ax = plt.subplots()
        numeric_df = df.select_dtypes(include=['int64', 'float64'])
    
        if numeric_df.shape[1] > 1:
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Not enough numeric columns for heatmap")

    # Insights
    st.subheader("📌 Insights")

    if len(numeric_cols) > 0:
        st.write(f"Mean of {column}: ", df[column].mean())
        st.write(f"Max of {column}: ", df[column].max())
        st.write(f"Min of {column}: ", df[column].min())
        st.write(f"Standard Deviation: ", df[column].std())

    # Extra feature
    st.subheader("🔍 Missing Values")
    st.write(df.isnull().sum())

else:
    st.info("👆 Upload a CSV file to get started!")