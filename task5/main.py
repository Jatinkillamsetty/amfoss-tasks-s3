# main file to run timetickquiz-2 pro
from user_profile import UserProfile
from quiz_engine import QuizEngine
from rich.console import Console
from utils import get_categories


console = Console()

def main():
    console.print("[bold blue]welcome to timetickquiz pro![/bold blue]")
    # write u r code here to:
    # - prompt for username
    # - create user profile
    # - get quiz settings (num questions, difficulty, time limit)
    # - show categories and let user pick one
    # - start the quizlty
    username=console.input("Enter name")
    
    
    num_questions=int(console.input("choose number of questions"))
    time_limit=int(console.input("choose the time limit"))
    profile=UserProfile(username)
    difficulty=profile.adapt_difficulty()
    categories = get_categories()
    for c in categories:
        console.print(f"{c['id']}: {c['name']}")
    category_id = int(console.input("Choose category id: "))
    start=QuizEngine(profile, num_questions, difficulty, time_limit, category_id)
    scoret=start.run()
    print("The score of this quiz")
    print(scoret)
    profile.score += scoret 
    profile.save()
    return scoret
    




if __name__ == "__main__":
    main()