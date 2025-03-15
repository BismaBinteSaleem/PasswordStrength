
import streamlit as st
from passwordChecker import check_password_strength

st.markdown("""
    <style>
       .stTextInput >div>div>input {
            border: 2px solid #ADD8E6;                  /* Light blue outline */
            color: black;                               /* Black font color */
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #ADD8E6;                   /* Light blue  */
            color: black;                                /* Black font color */
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Password Strength Checker 🛡️")
    st.write("Enter your password below to check its strength:")

    password = st.text_input("Password 🔒",type="password")


    if st.button("Check Strength 💪"):
        strength,feedback= check_password_strength(password)
        st.success(f"Password Strength: {strength} 💥")

        if strength != "Extremely Strong":
           for message in feedback:
            st.write(message)


main()       


