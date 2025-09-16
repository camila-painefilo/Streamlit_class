import streamlit as st

# -------------------------------
# Custom CSS for Styling (IBA + PNU theme)
# -------------------------------
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background-color: #FFFFFF;
    }

    /* Titles */
    h1, h2, h3 {
        color: #2E5FA7; /* Azul IBA */
    }

    /* Buttons */
    .stButton button {
        background-color: #2E5FA7;
        color: white;
        border-radius: 10px;
    }
    .stButton button:hover {
        background-color: #2CA46C; /* Verde PNU */
        color: white;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        color: #2E5FA7;
        font-size: 14px;
        border-top: 1px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Title and Introduction
# -------------------------------
st.image("https://upload.wikimedia.org/wikipedia/en/4/44/Pusan_National_University.png", width=120)
st.title("Simple Streamlit App")
st.subheader("Assignment 1 - Pusan National University")

st.write("""
This web application demonstrates basic Streamlit functionality:
1. Enter two numbers (A and B) and calculate their sum.  
2. Select one of the numbers and calculate the sum of all integers up to that number.  
""")

st.divider()

# -------------------------------
# Section 1: Sum of Two Numbers
# -------------------------------
st.header("Step 1: Add Two Numbers")
a = st.number_input("Enter number A", min_value=0, step=1)
b = st.number_input("Enter number B", min_value=0, step=1)

sum_ab = a + b
st.metric(label="Sum of A and B", value=sum_ab)

st.divider()

# -------------------------------
# Section 2: Cumulative Sum
# -------------------------------
st.header("Step 2: Sum of All Integers Up to a Selected Number")
selected_value = st.selectbox("Select a number (A or B)", options=[("A", a), ("B", b)], format_func=lambda x: x[0])

label, chosen_number = selected_value
cumulative_sum = sum(range(1, int(chosen_number) + 1))

st.metric(label=f"Cumulative Sum up to {label}", value=cumulative_sum)

st.divider()

# -------------------------------
# Footer
# -------------------------------
st.markdown(
    """
    <div class="footer">
        Developed by <strong>Camila Estefanía Painefilo Hermosilla</strong> | IBA Lab - Pusan National University
    </div>
    """,
    unsafe_allow_html=True
)



