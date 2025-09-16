import streamlit as st

# -------------------------------
# Title and Introduction
# -------------------------------
st.title("Simple Streamlit App")
st.subheader("Assignment 1 - Pusan National University")

st.write("""
This web application demonstrates basic Streamlit functionality:
1. Enter two numbers (A and B) and calculate their sum.  
2. Select one of the numbers and calculate the sum of all integers up to that number.  
""")

# -------------------------------
# Section 1: Sum of Two Numbers
# -------------------------------
st.header("Step 1: Add Two Numbers")
st.write("Enter values for **A** and **B** to calculate their sum.")

# Input fields (you can use text_input or number_input)
a = st.number_input("Enter number A", min_value=0, step=1)
b = st.number_input("Enter number B", min_value=0, step=1)

# Calculate and display result
sum_ab = a + b
st.success(f"The sum of A and B is: **{sum_ab}**")

# -------------------------------
# Section 2: Sum of Numbers Up to Selected Value
# -------------------------------
st.header("Step 2: Sum of All Integers Up to a Selected Number")
st.write("Choose either A or B, then calculate the cumulative sum up to that number.")

# Selectbox to choose between A and B
selected_value = st.selectbox("Select a number (A or B)", options=[("A", a), ("B", b)], format_func=lambda x: x[0])

# Extract the chosen number
label, chosen_number = selected_value

# Calculate cumulative sum
cumulative_sum = sum(range(1, int(chosen_number) + 1))

st.info(f"The sum of all integers from 1 to {label} ({int(chosen_number)}) is: **{cumulative_sum}**")


