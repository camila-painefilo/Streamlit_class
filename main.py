import streamlit as st

# ===============================
# THEME / BASE STYLES (IBA + PNU)
# ===============================
st.markdown(
    """
    <style>
    /* Reset background */
    .stApp { background: #FFFFFF; }

    /* Header banner with gradient (PNU blues) */
    .header-banner {
        width: 100%;
        margin: 0 0 18px 0;
        background: linear-gradient(90deg, #2E5FA7 0%, #4F86C6 60%, #7BA6D8 100%);
        color: #ffffff;
        border-radius: 14px;
        padding: 22px 18px;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }
    .header-banner h1 {
        margin: 0;
        font-size: 32px;
        line-height: 1.15;
        font-weight: 800;
    }
    .header-banner p {
        margin: 6px 0 0 0;
        font-size: 15px;
        opacity: 0.95;
    }

    /* Section headings */
    h2, h3 { color: #2E5FA7; }

    /* Buttons */
    .stButton button {
        background-color: #2E5FA7;
        color: #ffffff;
        border-radius: 10px;
    }
    .stButton button:hover {
        background-color: #2CA46C;  /* green accent */
        color: #ffffff;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        text-align: center;
        padding: 10px 12px;
        background: #FFFFFF;   /* white so it doesn't overlap dark areas */
        border-top: 1px solid #e6e6e6;
        color: #2E5FA7;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================
# HEADER (centered)
# ================
st.markdown(
    """
    <div class="header-banner">
        <h1>Simple Streamlit App</h1>
        <p>Assignment 1 · AI Programming</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------
# App description
# --------------
st.write(
    """
This web application demonstrates basic Streamlit functionality:
1) Enter two numbers (A and B) and calculate their sum.  
2) Select one of the numbers and calculate the sum of all integers up to that number.
"""
)

st.divider()

# ==============================
# Step 1: Add two numbers (A, B)
# ==============================
st.header("Step 1: Add Two Numbers")
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Enter number A", min_value=0, step=1)
with col2:
    b = st.number_input("Enter number B", min_value=0, step=1)

sum_ab = a + b
st.metric(label="Sum of A and B", value=int(sum_ab) if float(sum_ab).is_integer() else sum_ab)

st.divider()

# =====================================================
# Step 2: Sum of all integers up to the selected number
# =====================================================
st.header("Step 2: Sum of All Integers Up to a Selected Number")
selected = st.selectbox(
    "Select a number (A or B)",
    options=[("A", a), ("B", b)],
    format_func=lambda x: x[0]
)

label, chosen = selected
cumulative_sum = sum(range(1, int(chosen) + 1)) if chosen >= 1 else 0
st.metric(label=f"Cumulative Sum up to {label}", value=cumulative_sum)

st.divider()

# -------
# Footer
# -------
st.markdown(
    """
    <div class="footer">
        Developed by <strong>Camila Estefanía Painefilo Hermosilla</strong>
    </div>
    """,
    unsafe_allow_html=True
)

