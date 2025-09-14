# manages user profiles
import json
from utils import get_profile, update_profile
from quiz_engine import QuizEngine

class UserProfile:
    def __init__(self, username):
        # write u r code here to:
        # - load existing profile or create new one
        # - set username, score, high score, difficulty
        self.username=username
        #self.score=0
        result=get_profile(self.username)
        #self.score=result.get('score')
        if result is None:   
            self.score = 0
            self.high_score = 0
            self.difficulty = "easy"
            self.save()
        else:                
            self.score = result.get("score", 0)
            self.high_score = result.get("high_score", 0)
            self.difficulty = result.get("difficulty", "easy")
        


    def increase_score(self):
        # write u r code here to:
        # - increase score
        # - update high score if needed
        # - adapt difficulty based on score
        # - save profile
        self.score=self.score+1
        self.save()
        return self.score

     
    def adapt_difficulty(self):
        # write u r code here to:
        # - adjust difficulty based on score (e.g., hard if score > 50)
        if self.score>=0 and self.score<10:
            return "easy"
        elif self.score>=10 and self.score<15:
            return "medium"
        elif self.score>=15:
            return "hard"

    def save(self):
        # write u r code here to:
        # - save profile to profiles.json
        
        try:
            with open("profiles.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        if self.username not in data:
            data[self.username] = {}

        data[self.username]["score"] = self.score
        
        data[self.username]["difficulty"] = self.difficulty

        with open("profiles.json","w") as file:
            json.dump(data, file, indent=4)
