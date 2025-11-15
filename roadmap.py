import json

with open("models/roles_skills.json", "r") as f:
    skills_for_roles = json.load(f)

def generate_roadmap(user_input):
    current_skills = set(user_input.get('current_skills', []))
    target_role = user_input.get('target_role', '')
    all_skills = set(skills_for_roles.get(target_role, []))
    
    skill_gap = all_skills - current_skills
    weeks = user_input.get('time_frame_weeks', 12)
    hours_per_week = user_input.get('learning_hours_per_week', 10)
    
    roadmap = []
    if skill_gap:
        skill_list = list(skill_gap)
        per_skill_weeks = max(1, weeks // len(skill_list))
        for i, skill in enumerate(skill_list):
            roadmap.append({
                "skill": skill,
                "start_week": i * per_skill_weeks + 1,
                "end_week": min((i+1) * per_skill_weeks, weeks),
                "hours_per_week": hours_per_week
            })
    return roadmap
