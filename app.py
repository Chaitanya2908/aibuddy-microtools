import streamlit as st

st.set_page_config(page_title="AI Buddy Resume Generator", page_icon="📝")

st.title("📝 AI Buddy Resume Generator")

st.markdown("Fill in the details below and get a simple formatted resume preview.")

with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    summary = st.text_area("Professional Summary")
    skills = st.text_area("Skills (comma separated)")
    experience = st.text_area("Work Experience")

    submitted = st.form_submit_button("Generate Resume")

if submitted:
    st.header(f"Resume for {name}")
    st.markdown(f"**Email:** {email}")
    st.markdown(f"**Phone:** {phone}")
    st.markdown(f"---")
    st.subheader("Professional Summary")
    st.write(summary)
    st.subheader("Skills")
    st.write(", ".join([skill.strip() for skill in skills.split(",") if skill.strip()]))
    st.subheader("Work Experience")
    st.write(experience)
