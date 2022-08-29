from pathlib import Path
import streamlit as st
from PIL import Image


# ---  Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Data Scientist CV | Danilo Andrade"
PAGE_ICON = ":wave:"
NAME = "Danilo Andrade"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "danilo_as@live.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCY-3XHPJ3T9i21Vb76_DG3A",
    "LinkedIn": "https://www.linkedin.com/in/daniloandradesantos/",
    "GitHub": "https://github.com/daniloasdotcom",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://biochar.herokuapp.com/",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://calagemapp.com/",
}

st.set_page_config(page_title=PAGE_TITLE,
                   page_icon=PAGE_ICON,
                   )

# --- Load CSS, PDF e PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("", EMAIL)


# --- Social Links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️7 Years expereince extracting actionable insights from data
- ✔️Strong hands on experience and knowledge in Python and Excel
- ✔️Good understanding of statistical principles and their respective applications
- ✔️Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: MS Excel, Rbase, ggplot2
- 📚 Modeling: Linear regression, Non-linear-regression
"""
)















