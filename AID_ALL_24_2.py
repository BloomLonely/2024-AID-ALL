import os
import streamlit as st
import pandas as pd
import requests


# github_token = st.secrets["GITHUB_TOKEN"]
# headers = {"Authorization": f"token {github_token}"}

exam_title = "2024 Fall Artificial Intelligence Design Grading Results"
fname_midterm = "aid_midterm.xlsx"
fname_final = "aid_final.xlsx"
fname_quiz_attendence = "aid_quiz_attendence.xlsx"
fname_assignment = "aid_assignment.xlsx"
#response = requests.get(fname, headers=headers)
solution1 = '''
### 중간고사 (Midterm Exam)
'''
solution2 = '''
### 기말고사 (Final Exam)
'''
solution3 = '''
### 퀴즈 + 출석 (Quiz + Attendence)
'''
solution4 = '''
### 숙제 (Assignment)
In Class Assignment, After Class Assignment, Homework
'''

# Setup Title & Wide layout
st.set_page_config(page_title=exam_title, layout="wide")
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size:1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Load the Excel data
df_midterm = pd.read_excel(fname_midterm, dtype={'Student ID': 'Int64', '1 - 10p': 'Int64', '2 - 8p': 'Int64', '3 - 10p': 'Int64', '4 - 8p': 'Int64', '5 - 10p': 'Int64', '6 - 14p': 'Int64', '7 - 15p': 'Int64', '8 - 12p': 'Int64', '9 - 13p': 'Int64', '총점': 'Int64'})
df_final = pd.read_excel(fname_final, dtype={'Student ID': 'Int64', '1 - 10p': 'Int64', '2 - 8p': 'Int64', '3 - 10p': 'Int64', '4 - 8p': 'Int64', '5 - 10p': 'Int64', '6 - 14p': 'Int64', '7 - 15p': 'Int64', '8 - 12p': 'Int64', '9 - 13p': 'Int64', '총점': 'Int64'})
df_quiz_attendence = pd.read_excel(fname_quiz_attendence, dtype={'Student ID': 'Int64', '1 - 10p': 'Int64', '2 - 8p': 'Int64', '3 - 10p': 'Int64', '4 - 8p': 'Int64', '5 - 10p': 'Int64', '6 - 14p': 'Int64', '7 - 15p': 'Int64', '8 - 12p': 'Int64', '9 - 13p': 'Int64', '총점': 'Int64'})
df_assignment = pd.read_excel(fname_assignment, dtype={'Student ID': 'Int64', '1 - 10p': 'Int64', '2 - 8p': 'Int64', '3 - 10p': 'Int64', '4 - 8p': 'Int64', '5 - 10p': 'Int64', '6 - 14p': 'Int64', '7 - 15p': 'Int64', '8 - 12p': 'Int64', '9 - 13p': 'Int64', '총점': 'Int64'})

def get_student_data(student_id):
    """
    Fetch the data for a given student ID from the Excel file.
    
    Args:
    - student_id (int): The ID of the student.
    
    Returns:
    - pd.DataFrame or None: The data for the student if found, otherwise None.
    """
    student_data = df[df["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None

# Streamlit app layout and logic
st.title(exam_title)

# Get the student ID from the user
student_id = st.text_input("Please enter your email and press the Enter key.", value='hwanheelee@cau.ac.kr')

# When the user provides a student ID, fetch and display the data
if student_id:
    data = get_student_data(student_id)
    
    if data is not None:
        filtered_data = data[["Name", "Student ID", "1 - 10p", "2 - 8p", "3 - 10p", "4 - 8p", "5 - 10p", "6 - 14p", "7 - 15p", "8 - 12p", "9 - 13p", "총점"]]
        filtered_data["Student ID"] = filtered_data["Student ID"].astype(str)
        st.write("E-mail: ", student_id)
        st.dataframe(filtered_data, hide_index=True)
    else:
        st.write(f"No data found for email: {student_id}")


st.write(solution1)
if student_id:
    if data is not None:
        st.markdown("#### Question1. Student's Detailed Score")
        student_answers = data[["1 - a", "1 - b", "1 - c", "1 - d", "1 - e", "1 - 10p"]].copy()
        st.dataframe(student_answers, hide_index=True)

st.write(solution2)
if student_id:
    if data is not None:
        st.markdown("#### Question2. Student's Detailed Score")
        student_answers = data[["2 - a", "2 - b", "2 - c", "2 - d", "2 - 8p"]].copy()
        st.dataframe(student_answers, hide_index=True)

st.write(solution3)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question3. Student's Detailed Score")
        student_answers = data[["3 - a", "3 - b", "3 - c", "3 - 10p"]]
        st.dataframe(student_answers, hide_index=True)

st.write(solution4)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question4. Student's Detailed Score")
        student_answers = data[["4 - a", "4 - b", "4 - 8p"]]
        st.dataframe(student_answers, hide_index=True)

st.write(solution5)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question5. Student's Detailed Score")
        student_answers = data[["5 - a", "5 - b", "5 - 10p"]]
        st.dataframe(student_answers, hide_index=True)

st.write(solution6)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question6. Student's Detailed Score")
        student_answers = data[["6 - a", "6 - b", "6 - c", "6 - 14p"]]
        st.dataframe(student_answers, hide_index=True)

st.write(solution7)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question7. Student's Detailed Score")
        student_answers = data[["7 - a", "7 - b", "7 - 15p"]]
        st.dataframe(student_answers, hide_index=True)

st.write(solution8)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question8. Student's Detailed Score")
        student_answers = data[["8 - a", "8 - b", "8 - 12p"]]
        st.dataframe(student_answers, hide_index=True)

st.write(solution9)
if student_id:
    data = get_student_data(student_id)
    if data is not None:
        st.markdown("#### Question9. Student's Detailed Score")
        student_answers = data[["9 - a", "9 - b", "9 - c", "9 - 13p"]]
        st.dataframe(student_answers, hide_index=True)
