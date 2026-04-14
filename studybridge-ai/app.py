import streamlit as st
from planner_engine import generate_plan

st.set_page_config(page_title="StudyBridge AI", layout="centered")

st.title("📚 StudyBridge AI")
st.subheader("AI-Powered Personalized Study Planner")

st.write("Enter your subjects, study hours, and exam date to get a smart study plan.")

subjects = st.text_input(
    "Enter subjects (comma separated):",
    placeholder="Example: Java, DBMS, OS"
)

hours_per_day = st.number_input(
    "Hours available per day:",
    min_value=1,
    max_value=24,
    value=4
)

exam_date = st.date_input("Select exam date:")

if st.button("Generate Study Plan"):
    if subjects.strip() == "":
        st.warning("Please enter at least one subject.")
    else:
        result = generate_plan(subjects, hours_per_day, str(exam_date))
        
        if result:
            st.success(f"📅 {result['days_left']} days left for exam")
            st.info(f"⏳ Total study hours available: {result['total_hours']} hours")
            
            st.subheader("📖 Your Study Plan")
            
            for subject, details in result["plan"].items():
                st.markdown(f"### {subject}")
                st.write(f"⏱️ Hours per topic: {details['hours_per_topic']}")
                
                for topic in details["topics"]:
                    st.write(f"• {topic}")
                
                st.divider()
        else:
            st.error("Exam date should be in the future.")
