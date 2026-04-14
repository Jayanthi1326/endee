import streamlit as st
from roadmap_engine import analyze_skills

st.set_page_config(page_title="MentorBridge AI", layout="centered")

st.title("🚀 MentorBridge AI")
st.subheader("AI-Powered Learning Roadmap Generator")

st.write("Enter your current skills and career goal to get a personalized roadmap.")

# Input fields
skills = st.text_input(
    "Enter your skills (comma separated):",
    placeholder="Example: Java, HTML, CSS"
)

goal = st.selectbox(
    "Select your target role:",
    ["Full Stack Developer", "Backend Developer", "Data Analyst"]
)

if st.button("Generate Roadmap"):
    if skills.strip() == "":
        st.warning("Please enter your skills.")
    else:
        result = analyze_skills(skills, goal)

        if result:
            st.success(f"🎯 Role Match: {result['match_percent']}%")

            st.subheader("✅ Skills You Already Have")
            if result["matched"]:
                for skill in result["matched"]:
                    st.write(f"✔ {skill}")
            else:
                st.write("No matching skills found.")

            st.subheader("📚 Skills You Need to Learn")
            for skill in result["missing"]:
                st.write(f"🔹 {skill}")

            st.subheader("💡 Suggested Mini Projects")
            for project in result["projects"]:
                st.write(f"📌 {project}")
