diary_entries = {}  # key = user_id

def add_diary_entry(user_id, week, skills, hours):
    if user_id not in diary_entries:
        diary_entries[user_id] = []
    diary_entries[user_id].append({
        "week": week,
        "skills_practiced": skills,
        "hours": hours
    })

def get_diary(user_id):
    return diary_entries.get(user_id, [])
