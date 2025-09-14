# utility functions for quiz
import json
import os
import requests

PROFILE_FILE = os.path.join(os.path.dirname(__file__), '../profiles.json')
CATEGORY_URL = "https://opentdb.com/api_category.php"


def load_profiles():
    # write u r code here to:
    # - load profiles from profiles.json
    # - return profiles list
    if not os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "w") as f:
            json.dump({}, f, indent=4)
        return {}
    
    with open(PROFILE_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    return data
def save_profiles(profiles):
    # write u r code here to:
    # - save profiles to profiles.json
    with open(PROFILE_FILE, "w") as f:
        json.dump(profiles, f, indent=4)

def get_profile(username):
    # write u r code here to:
    # - find profile by username
    # - return profile or None
    profiles = load_profiles()
    return profiles.get(username)
         

def update_profile(new_profile):
    # write u r code here to:r
    # - update or add profile to profiles.json
    profiles = load_profiles()
    profiles[new_profile["name"]] = new_profile
    save_profiles(profiles)


def get_categories():
    # write u r code here to:
    # - fetch categories from CATEGORY_URL
    # - handle errors and return categories list
    try:
        response = requests.get(CATEGORY_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("trivia_categories", [])
    except Exception as e:
        print(f"Error ")
        return []