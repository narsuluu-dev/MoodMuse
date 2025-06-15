# Phase 1. Create basic file and setup input/output
# Welcoming message
print("Welcome to Mood Muse!")

def main():  
    name, mood, reflection = get_user_input()
    song, quote = suggest_content(mood)

    print(f"\nSong: {song}\n")
    print(f"Quote: {quote}\n")

    save_to_journal(name, mood, reflection, song, quote)

def get_user_input():
    name = input("Enter your name:  ") 
    mood = input("Tell us your mood [ happy, tired, sad, anxious]:  ")
    reflection = input("How are you feeling right now?:  ")  

    return name, mood, reflection 

   
# Phase 2. Create Mood - Based Content 

def suggest_content(mood): 

# Create dictionaries of suggested songs, quotes based on a user's mood
    mood_data = {
    "sad": {
        "songs": ["BTS-Black Swan", "BTS-Fake Love"],
        "quote":"It's okay not to be okay. Just don't give up."
     }, 
    "happy": {
    "songs": ["BTS-Magic Shop", "BTS-Love Myself"], 
    "quote": "The most important thing is to enjoy your life - to be happy"
     }, 

    "tired": {
    "songs": ["Jung Kook-Still With You",  "Suga-Shadow" ], 
    "quote": "You don't have to be strong" 

     }, 
     "anxious": {
    "songs": ["Breathe", "Lonely",  "Mikrokosmos"], 
    "quote": "You don't have to control your thoughts. You just have to stop letting them control you"

  }
     }

    if mood in mood_data: 
        from random import choice
        song = choice(mood_data[mood]["songs"])
        quote = mood_data[mood]["quote"] 
        return song, quote 
    
    else: 
        return "Lo-fi beats playlist", 'Feel your feelings. Then keep going'



from datetime import datetime, date, time, timedelta 




# Get current date and time
now = datetime.now()
print(f"Date and time: {now}") 

#Phase 3. Save user's inputs into the file and gave as a journal 

def save_to_journal(name, mood, reflection, song, quote): 
    now = datetime.now()
    with open ("moodemuse_journal.txt", "a", encoding= "utf-8") as file:
        file.write(f"--Entry on {now}--\n")
        file.write(f"Name: {name}\n")
        file.write(f"Mood: {mood}\n")
        file.write(f"Reflection: {reflection}\n")
        file.write(f"Suggested Song:{song}\n")
        file.write(f"Quote: {quote}\n\n")

        


main()
  




    


