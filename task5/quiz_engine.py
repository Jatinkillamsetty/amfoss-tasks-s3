# handles quiz logic and api calls
import requests
import html
import threading
import time
from time import *
from rich.console import Console

console = Console()
CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"

class QuizEngine:
    def __init__(self, profile, num_questions, difficulty, time_limit, category_id):
        self.profile = profile
        self.num_questions = num_questions
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.category_id = category_id
        self.questions = []
        self.time_up = False

        self.score = profile.score

    def fetch_questions(self):
        # write u r code here to:
        # - build params for api call
        # - fetch questions from QUESTION_URL
        # - handle errors and store question
        try:
            response = requests.get(f"https://opentdb.com/api.php?amount={self.num_questions}&category={self.category_id}&difficulty={self.difficulty}&type=multiple"
)

            data=response.json()
            self.questions=data['results']
            
        except Exception as e:
            console.print(f"[red]Error fetching questions: {e}[/red]")
            return []
    

    def ask_question(self):
        # write u r code here to:
        # - decode question and answers
        # - show question and options
        # - use threading to enforce time limit
        # - get user input and check if correct
        # - return True for correct, False for incorrect
        pass
        
        
    def run(self):
        # write u r code here to:
        # - fetch questions
        # - loop through questions and ask them
        # - update score and show final results
        
        def countdown():
            sleep(self.time_limit)
            self.time_up = True
            console.print("[yellow]\n Time up![/yellow]")
            console.print("[cyan]Retry agin[/cyan]")
        
        
        thread_count = threading.Thread(target=countdown)
        thread_count.start()

        
        
        self.fetch_questions()
        
        for i,question in enumerate(self.questions):
            if self.time_up:  
                break
            
            console.print(f"[bold blue]{i} {question['question']}[/bold blue]")

            options=[]
            correct = question["correct_answer"]
            options = question["incorrect_answers"].copy()
            options.append(correct)

            import random
            random.shuffle(options)
            for j,option in enumerate(options):
                print(f'{j+1} {option}')
            if self.time_up:
                break
            answer=int(input("Enter your answer from 1 to4"))
            if self.time_up:
                break
            if options[answer-1]==question['correct_answer']:
                console.print("[green]Correct Answer![/green]")
                self.profile.increase_score()   
            elif options[answer-1] in question['incorrect_answers']:
                console.print("[red]Wrong Answer![/red]")
        
        return self.profile.score

    



