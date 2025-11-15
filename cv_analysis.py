import spacy
import json

nlp = spacy.load("en_core_web_sm")

with open("models/roles_skills.json", "r") as f:
    role_skills_db = json.load(f)

skill_keywords = set([skill for skills in role_skills_db.values() for skill in skills])

def extract_skills(cv_text):
    doc = nlp(cv_text.lower())
    tokens = [token.text for token in doc if not token.is_stop]
    matched_skills = [skill for skill in skill_keywords if skill.lower() in tokens]
    return list(set(matched_skills))
