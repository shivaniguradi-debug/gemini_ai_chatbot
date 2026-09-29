import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# --------------------------------------------------
# LOAD API KEY
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="✦",
    layout="centered"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* =========================================
   COLORFUL LIGHT BACKGROUND
   ========================================= */

.stApp {
    background:
        radial-gradient(
            circle at 8% 12%,
            #ffd6e7 0%,
            transparent 25%
        ),
        radial-gradient(
            circle at 92% 10%,
            #c9f3ff 0%,
            transparent 25%
        ),
        radial-gradient(
            circle at 8% 88%,
            #ddd2ff 0%,
            transparent 25%
        ),
        radial-gradient(
            circle at 92% 88%,
            #fff0b8 0%,
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #fff9fc,
            #f4f8ff,
            #faf5ff
        );
}


/* =========================================
   MAIN CONTAINER
   ========================================= */

.block-container {
    max-width: 950px;
    padding-top: 35px;
    padding-bottom: 40px;
}


/* =========================================
   TITLE
   ========================================= */

h1 {
    text-align: center !important;

    color: #7c3aed !important;

    font-size: 45px !important;

    font-weight: 800 !important;

    margin-bottom: 5px !important;
}


/* =========================================
   SUBTITLE
   ========================================= */

.subtitle {
    text-align: center;

    color: #475569;

    font-size: 20px;

    margin-bottom: 40px;
}


/* =========================================
   PROMPT LABEL
   ========================================= */

.stTextArea label {
    color: #1e293b !important;

    font-size: 17px !important;

    font-weight: 700 !important;
}


/* =========================================
   TEXT AREA
   ========================================= */

textarea {

    background-color: #ffffff !important;

    color: #1e293b !important;

    border: 2px solid #c4b5fd !important;

    border-radius: 14px !important;

    font-size: 16px !important;

    padding: 15px !important;

    box-shadow:
        0 8px 25px rgba(124, 58, 237, 0.10) !important;
}


/* Placeholder */

textarea::placeholder {
    color: #94a3b8 !important;
}


/* Focus */

textarea:focus {

    border: 2px solid #a855f7 !important;

    box-shadow:
        0 0 0 4px rgba(168, 85, 247, 0.12) !important;
}


/* =========================================
   BUTTON
   ========================================= */

.stButton {
    margin-top: 20px;
}


.stButton > button {

    width: 100%;

    background: linear-gradient(
        90deg,
        #7c3aed,
        #ec4899
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding: 13px 25px !important;

    font-size: 17px !important;

    font-weight: 600 !important;

    box-shadow:
        0 7px 20px rgba(236, 72, 153, 0.22) !important;

    transition: all 0.3s ease !important;
}


.stButton > button:hover {

    background: linear-gradient(
        90deg,
        #6d28d9,
        #db2777
    ) !important;

    transform: translateY(-2px);

    box-shadow:
        0 10px 25px rgba(124, 58, 237, 0.25) !important;
}


/* =========================================
   RESPONSE TITLE
   ========================================= */

.response-heading {

    color: #7c3aed;

    font-size: 22px;

    font-weight: 700;

    margin-top: 25px;

    margin-bottom: 10px;
}


/* =========================================
   RESPONSE BOX
   ========================================= */

.response-box {

    background: rgba(255, 255, 255, 0.96);

    color: #1e293b;

    padding: 22px;

    border-radius: 15px;

    border-left: 5px solid #a855f7;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.07);

    line-height: 1.7;

    font-size: 16px;
}


/* =========================================
   FOOTER
   ========================================= */

.footer {

    text-align: center;

    color: #64748b;

    font-size: 14px;

    margin-top: 60px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("✦ Gemini AI Chatbot")

st.markdown(
    '<div class="subtitle">Ask Gemini anything! ✨</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# PROMPT
# --------------------------------------------------

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="💡 Example: Explain Artificial Intelligence",
    height=150
)


# --------------------------------------------------
# GENERATE RESPONSE
# --------------------------------------------------

if st.button("✨ Generate Response"):

    if prompt:

        try:

            with st.spinner("Gemini is thinking..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.success("Response generated !")

            st.markdown(
                '<div class="response-heading">'
                '✦ Gemini Response'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="response-box">'
                f'{response.text}'
                f'</div>',
                unsafe_allow_html=True
            )

        except Exception as e:

            st.error(
                "Something went wrong while connecting to Gemini."
            )

            st.code(str(e))

    else:

        st.warning("please enter a prompt.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Powered by Google Gemini ✨'
    '</div>',
    unsafe_allow_html=True
)