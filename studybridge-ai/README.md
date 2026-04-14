🚀 StudyBridge AI – Personalized Study Planner
📌 Overview
StudyBridge AI is an AI-powered web application designed to help students create personalized study plans based on their subjects, available study hours, and exam dates.
It provides a smart roadmap for efficient preparation by allocating time subject-wise and topic-wise.
🎯 Objective
To help students improve exam preparation through structured study schedules and time management using simple AI-based planning logic.
✨ Features
• Personalized daily study schedule
• Subject-wise topic breakdown
• Smart time allocation based on exam date
• Exam countdown tracker
• Easy-to-use interface
🛠️ Technologies Used
• Python Software Foundation
• Streamlit
• JSON (for syllabus dataset)
⚙️ How It Works
User enters subjects (comma separated)
User selects available study hours per day
User chooses exam date
System calculates days remaining
Study hours are distributed across subjects and topics
A personalized study plan is generated
📁 Project Structure
studybridge-ai/
│
├── app.py
├── planner_engine.py
├── requirements.txt
├── README.md
│
└── data/
  └── syllabus.json
▶️ How to Run
Clone repository:
git clone 
Install dependencies:
pip install -r requirements.txt
Run application:
streamlit run app.py
📊 Sample Output
Input:
Subjects: Java, DBMS, OS
Hours per day: 4
Exam date: 20 days from now
Output:
• 20 days left for exam
• Total study hours available: 80 hours
• Java: 5 hours/topic
• DBMS: 5 hours/topic
• OS: 5 hours/topic
📸 Demo
Add screenshots here: • Home page
• Input form
• Generated study plan
🔮 Future Enhancements
• AI-based weak topic detection
• Reminder notifications
• Progress tracker
• Study performance analytics
🏁 Conclusion
StudyBridge AI simplifies exam preparation by providing an intelligent and structured study roadmap.
It demonstrates practical use of AI concepts in student productivity and educational planning.
