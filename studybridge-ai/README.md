📚 StudyBridge AI – Personalized Study Planner

📌 Overview
StudyBridge AI is an AI-powered personalized study planner designed to help students prepare smarter for exams. By analyzing the subjects entered by the user, available study hours per day, and exam date, the system generates a structured and efficient study roadmap.
This system helps students to:
✨ Prioritize important subjects
⏳ Manage time effectively
📖 Cover topics systematically
🎯 Improve consistency and exam readiness

🎯 Objective
To help students create an efficient, personalized study schedule using simple AI-based planning logic and smart time allocation.

🚀 Features
📅 Personalized daily study schedule
📚 Subject-wise topic breakdown
⏱️ Smart time allocation based on exam date
🧠 Organized and efficient learning roadmap
⌛ Exam countdown tracker
💡 Beginner-friendly and easy-to-use interface

🛠️ Technologies Used
🐍 Python Software Foundation
🌐 Streamlit
🗂️ JSON for syllabus dataset

⚙️ How It Works
1️⃣ User enters subjects (comma separated)
2️⃣ User selects available study hours per day
3️⃣ User chooses exam date
4️⃣ System calculates days remaining for the exam
5️⃣ Total study hours are distributed subject-wise and topic-wise
6️⃣ A personalized study plan is generated instantly

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
🔹 Clone the repository:
git clone <your-repository-link>
🔹 Install dependencies:
pip install -r requirements.txt
🔹 Run the application:
streamlit run app.py

📊 Sample Input
📘 Subjects: Java, DBMS, OS
⏰ Hours per day: 4
📅 Exam date: 20 days from today

📈 Sample Output
✅ 20 days left for exam
⏳ Total study hours available: 80 hours
📖 Personalized subject-wise study plan generated

🔮 Future Enhancements
📌 AI-based weak topic detection
🔔 Smart revision reminders
📊 Progress tracking dashboard
🤖 AI chatbot study assistant

🏁 Conclusion
StudyBridge AI makes exam preparation easier and more organized by generating a smart and structured study roadmap. It demonstrates the practical use of AI concepts in educational planning and student productivity.
