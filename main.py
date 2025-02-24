import streamlit as st
import pandas as pd
import os
from io import BytesIO

def create_stremlit_app():
    st.set_page_config(page_title="Data Sweeper", page_icon="🧹", layout="wide")
    st.title("Data Sweeper")
    st.write("Transform your files between CSV and Excel formats with bulit-in data cleansing and visulization.")
    
    st.title("What would you like to do?")
    choice = st.radio("", ["Upload a file", "About"])
    
    if (choice == "Upload a file"):
        st.subheader("Upload a file")
        uploaded_files = st.file_uploader("Upload a file", type=["csv", "xlsx"], accept_multiple_files=True)
        
        if uploaded_files:
            for file in uploaded_files:
                file_ext = os.path.splitext(file.name)[-1].lower()
                
                if (file_ext == ".csv"):
                    df = pd.read_csv(file)
                elif (file_ext == ".xlsx"):
                    df = pd.read_excel(file)
                else:
                    st.error("Invalid file format. Please upload a CSV or Excel file.")
                    continue
                
                st.write(f"**File Name:** {file.name}")
                st.write(f"**File Size:** {file.size/1024}")
                
                st.write("Preview the top rows of file")
                st.dataframe(df.head())
                
                st.subheader("Data Cleansing Options")
                if st.checkbox(f"Clean Data for {file.name}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button(f"Remove Duplicates from {file.name}"):
                            df = df.drop_duplicates(inplace=True)
                            st.write("Duplicates removed successfully.")
                            
                    with col2:
                        if st.button(f"Fill Missing Values for {file.name}"):
                            numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
                            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                            st.write("Missing values filled successfully.")

                st.subheader("Select Coulmns to Convert")
                coulmns = st.multiselect(f"Choose Coulmns for {file.name}", df.columns, default=df.columns)
                df = df[coulmns]
                
                st.subheader(f"Data Visulization")
                
                if st.checkbox(f"Show Visulaization for {file.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
                    
                st.subheader("Conversion Options")
                conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "EXCEL"], key=file.name)
                if st.button(f"Convert {file.name}"):
                    buffer = BytesIO()
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False)
                        filename = file.name.replace(file_ext, ".csv")
                        mime_type = "text/csv"
                    elif conversion_type == "EXCEL":
                        df.to_excel(buffer, index=False)
                        filename = file.name.replace(file_ext, ".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    buffer.seek(0)
                    
                    
                    st.download_button(f"Download {file.name} as {conversion_type}", data=buffer, file_name=filename, mime=mime_type)
                    
            st.success("All tasks completed successfully.")
            
    else: 
        st.subheader("About")
        st.write("This is a simple data transformation tool that allows you to upload files in CSV or Excel format, cleanse the data, visualize the data, and download the data.")
        st.write("This tool is built using UV, Streamlit, Pandas.")
        st.write("Author: [Noman Haider](https://www.linkedin.com/in/nomanhaider99/)")



create_stremlit_app()