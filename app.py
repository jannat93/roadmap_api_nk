from flask import Flask, request, jsonify
from flask_cors import CORS
from cv_analysis import extract_skills
from roadmap import generate_roadmap
import diary_data

app = Flask(__name__)
CORS(app)  # Allow Flutter frontend to call API

# --- CV Analysis ---
@app.route("/analyze_cv", methods=["POST"])
def analyze_cv():
    data = request.get_json()
    cv_text = data.get("cv_text", "")
    skills = extract_skills(cv_text)
    return jsonify({"extracted_skills": skills})

# --- Roadmap Generation ---
@app.route("/generate_roadmap", methods=["POST"])
def roadmap_api():
    data = request.get_json()
    roadmap = generate_roadmap(data)
    return jsonify({"roadmap": roadmap})

# --- Diary ---
@app.route("/add_diary", methods=["POST"])
def add_diary():
    data = request.get_json()
    user_id = data.get("user_id", 0)
    week = data.get("week", 1)
    skills = data.get("skills_practiced", [])
    hours = data.get("hours", 0)
    diary_data.add_diary_entry(user_id, week, skills, hours)
    return jsonify({"status": "success"})

@app.route("/get_diary/<int:user_id>", methods=["GET"])
def get_diary(user_id):
    diary = diary_data.get_diary(user_id)
    return jsonify({"diary": diary})

if __name__ == "__main__":
    app.run(debug=True)
