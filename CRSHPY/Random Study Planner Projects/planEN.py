import random

# Data Storage
subjects = ["Math", "Science", "History", "English"]
study_moods = ("Focused", "Relaxed", "Motivated", "Lazy")

# Functions
def generate_timetable(subjects):
    timetable = {}
    for subject in subjects:
        study_time = random.randint(1, 3)  # Random hours
        timetable[subject] = f"{study_time} hour(s)"
    return timetable

def get_day_mood():
    return random.choice(study_moods)

# Main Program
print("Welcome to Random Study Planner!")

while True:
    print("\nMenu:")
    print("1. Generate Study Timetable")
    print("2. Check Today's Mood")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        timetable = generate_timetable(subjects)
        print("\nYour Study Timetable:")
        for subject, time in timetable.items():
            print(f"{subject}: {time}")
    
    elif choice == "2":
        mood = get_day_mood()
        print(f"\nToday's Mood: {mood}")
    
    elif choice == "3":
        print("Goodbye! Happy Studying!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
