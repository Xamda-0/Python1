# Random Study Planner Projects
# time
import random
subjects = ['physics',  'python','Math', 'Intro CS']
StudyMood = ['Marwalba hankaaga ha sarreeyo.', 'Tartanka ugu fiican oo aad gasho \nwaa kan aad naftaada la gasho.' ,'Dadaal hana niyadjabin.', 'Marwalba soo xasuuso inta wax oo quruxbadan oo aad ku guuleeysatay. ']
print('Kusoo dhawoow qaybta sammeeynta jadwalka.')

def time_table(subjects):
    timeTable = {}
    for subject in subjects:
        studyTime = random.randint(30, 30)
        timeTable[subject] = f"{studyTime} Minutes(s) "
    return timeTable
def get_day_mood():
    return random.choice(StudyMood)

while True:
    print("""
1. Sammeeynta Jadwalka.
2. Dhiirigelinta Maanta.
3. Exit.
""")
    jad_dooro = input('>>> Dooro dooqaada (1-3): ')

    if jad_dooro == "1":
        print("""
1. Subax 04:00 - 06:00 AM (2 Saacadood)
2. Galab 04:00 - 06:00 PM (2 Saacadood)
3. Habeen 08:00 - 10:00 PM (2 Saacadood)
""")
        free = int(input('>>> Dooro xilliga aad rabtid. '))
        timetable = time_table(subjects)
        print("\nYour Study Timetable:")
        for subject, time in timetable.items():
            print(f"{subject}: {time}")
            
    elif jad_dooro == "2":
        mood = get_day_mood()
        print(f"\nToday's Mood: {mood}")
    elif jad_dooro == "3":
        print("Goodbye! Happy Studying!")
        break
else:
    print("Invalid choice. Please enter a number between 1 and 3.")



print("""
1. Sammeeynta Jadwalka.
2. Dhiirigelinta Maanta.
3. Exit.
""")
jad_dooro = input('>>> Dooro dooqaada (1-3): ')
print("""
1. Subax 04:00 - 06:00 AM (2 Saacadood)
2. Galab 04:00 - 06:00 PM (2 Saacadood)
3. Habeen 06:00 - 10:00 PM (2 Saacadood)
""")
free = int(input('>>> Dooro xilliga aad rabtid. '))


if jad_dooro == "1":
        timetable = time_table(subjects)
        print("\nYour Study Timetable:")
        for subject, time in timetable.items():
            print(f"{subject}: {time}")
elif jad_dooro == "2":
        mood = get_day_mood()
        print(f"\nToday's Mood: {mood}")
elif jad_dooro == "3":
        print("Goodbye! Happy Studying!")
        # break
else:
        print("Invalid choice. Please enter a number between 1 and 3.")

