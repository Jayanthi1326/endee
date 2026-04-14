import json
from datetime import datetime

def load_syllabus():
    with open("data/syllabus.json", "r") as file:
        return json.load(file)

def generate_plan(subjects, hours_per_day, exam_date):
    syllabus = load_syllabus()
    
    selected_subjects = [sub.strip() for sub in subjects.split(",")]
    
    today = datetime.today()
    exam = datetime.strptime(exam_date, "%Y-%m-%d")
    days_left = (exam - today).days
    
    if days_left <= 0:
        return None
    
    total_hours = days_left * hours_per_day
    
    plan = {}
    
    for subject in selected_subjects:
        if subject in syllabus:
            topics = syllabus[subject]
            hours_per_topic = max(1, total_hours // (len(selected_subjects) * len(topics)))
            
            plan[subject] = {
                "topics": topics,
                "hours_per_topic": hours_per_topic
            }
    
    return {
        "days_left": days_left,
        "total_hours": total_hours,
        "plan": plan
    }
