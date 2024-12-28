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
fname_all = "aid_all.xlsx"
#response = requests.get(fname, headers=headers)
solution1 = '''
### 중간고사 (Midterm Exam) Full Result: 35
'''
solution2 = '''
### 기말고사 (Final Exam) Full Result: 35
'''
solution3 = '''
### 퀴즈 + 출석 (Quiz + Attendence) Full Result: 10
'''
solution4 = '''
### 숙제 (Assignment) Full Result: 20
#### In Class Assignment, After Class Assignment, Homework
'''
solution5 = '''
### 최종 결과 (Result of all) Full Result: 100
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
df_midterm = pd.read_excel(fname_midterm, dtype={ '1 - 10p': 'Int64', '2 - 12p': 'Int64', '3 - 8p': 'Int64', '4 - 12p': 'Int64', '5 - 12p': 'Int64', '6 - 18p': 'Int64', '7 - 14p': 'Int64', '8 - 8p': 'Int64', '9 - 6p': 'Int64', 'Score': 'Int64', 'Result': 'Float32'})
df_final = pd.read_excel(fname_final, dtype={'1 - 10p': 'Int64', '2 - 8p': 'Int64', '3 - 10p': 'Int64', '4 - 8p': 'Int64', '5 - 10p': 'Int64', '6 - 14p': 'Int64', '7 - 15p': 'Int64', '8 - 12p': 'Int64', '9 - 13p': 'Int64', 'Score': 'Int64', 'Result': 'Float32'})
df_quiz_attendence = pd.read_excel(fname_quiz_attendence)
df_assignment = pd.read_excel(fname_assignment, dtype={'In-class Assignment': 'Int64', 'After-class Assignment': 'Int64', 'Homework1': 'Int64', 'Homework2': 'Int64', 'Result': 'Float32'})
df_all = pd.read_excel(fname_all)

def get_student_data_midterm(student_id):
    student_data = df_midterm[df_midterm["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None
def get_student_data_final(student_id):
    student_data = df_final[df_final["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None
def get_student_data_quiz_attendence(student_id):
    student_data = df_quiz_attendence[df_quiz_attendence["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None
def get_student_data_assignment(student_id):

    student_data = df_assignment[df_assignment["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None
def get_student_data_all(student_id):

    student_data = df_all[df_all["e-mail"] == student_id]
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
    st.write(solution1)
    data_midterm = get_student_data_midterm(student_id)
    if data_midterm is not None:
        student_midterm = data_midterm[["Name", "Student ID", "1 - 10p", "2 - 12p", "3 - 8p", "4 - 12p", "5 - 12p", "6 - 18p", "7 - 14p", "8 - 8p", "9 - 6p", "Score", "Result"]].copy()
        student_midterm["Student ID"] = student_midterm["Student ID"].astype(str)
        st.dataframe(student_midterm, hide_index=True)

if student_id:
    st.write(solution2)
    data_final = get_student_data_final(student_id)
    if data_final is not None:
        student_final = data_final[["Name", "Student ID", "1 - 10p", "2 - 8p", "3 - 10p", "4 - 8p", "5 - 10p", "6 - 14p", "7 - 15p", "8 - 12p", "9 - 13p", "Score", "Result"]].copy()
        student_final["Student ID"] = student_final["Student ID"].astype(str)
        st.dataframe(student_final, hide_index=True)

if student_id:
    st.write(solution3)
    data_quiz_attendence = get_student_data_quiz_attendence(student_id)
    if data_quiz_attendence is not None:
        student_quiz_attendence = data_quiz_attendence[["Name", "Student ID", "Week 2", "Week 4", "Week 5", "Week 7", "Week 9", "Week 10", "Week 12", "Week 13", "Week 14", "Week 15", "Result"]]
        student_quiz_attendence["Student ID"] = student_quiz_attendence["Student ID"].astype(str)
        st.dataframe(student_quiz_attendence, hide_index=True)

if student_id:
    st.write(solution4)
    data_assignment = get_student_data_assignment(student_id)
    if data_assignment is not None:
        student_assignment = data_assignment[["Name", "Student ID", "In-Class Assignment", "After-Class Assignment", "Homework1", "Homework2", "Result"]]
        student_assignment["Student ID"] = student_assignment["Student ID"].astype(str)
        st.dataframe(student_assignment, hide_index=True)

if student_id:
    st.write(solution5)
    data_all = get_student_data_all(student_id)
    if data_all is not None:
        student_all = data_all[["Name", "Student ID", "Midterm", "Final", "Quiz+Attendence", "Assignment", "Result"]]
        student_all["Student ID"] = student_all["Student ID"].astype(str)
        st.dataframe(student_all, hide_index=True)
