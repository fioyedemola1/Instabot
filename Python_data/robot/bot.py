# library imports
import pyttsx3
import speech_recognition as sr
import random
# modules

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


def listen():
    mic = sr.Microphone()
    rec = sr.Recognizer()
    with mic as source:  # < context manager with
        talk('...listening')
        print('...listening')
        audio = rec.listen(source)
        try:
            word = rec.recognize_google(audio)
            talk(f'did you say {word}')
            return word


        except:
            talk('i did not get that')
            return listen()

#  skills --- play game, tell weather, quotes, time.....

def play_game():
    my_score = 0
    com_score = 0
    choices = ('rock', 'paper', 'scissors')
    talk(f'lets play a game of {choices}') 
    counter = 5 # tries
    while counter:
        talk('please select your choice')

        my_answer = listen().lower()
        check = [ True if x == my_answer else False  for x in choices]
        if not any(check):
            talk('you answer is invalid')
            continue
        computer = random.choice(choices)
        counter -=1
        talk(f'computer chose {computer} and you chose {my_answer}')
        if my_answer == computer: # rock == rock
            my_score+= 0.5
            com_score+= 0.5
            talk('its a tie half points earned')
        elif my_answer == 'rock':
            if computer == 'paper':
                talk('computer wins, one point earned')
                com_score += 1
            else:
                talk('you win, one point earned')
                my_score+= 1

        elif my_answer == 'paper':
            if computer == 'scissors':
                talk('computer wins, one point earned')
                com_score += 1
            else:
                talk('you win, one point earned')
                my_score+= 1
        elif my_answer == 'scissors':
            if computer == 'rock':
                talk('computer wins, one point earned')
                com_score += 1
            else:
                talk('you win, one point earned')
                my_score+= 1
    else:
        if my_score > com_score:
            talk(f'You won by {my_score} points')   
        elif my_score < com_score:
            talk(f'computer won by {com_score} points')   
        else:
            talk(f'It is a tie')   


def weather():
    print('weather')


# skill = [play_game,weather,quotes]
skill = {
    'game': lambda : play_game(),
    'weather':  lambda: weather()
}


while True:
    a = listen()
    if 'hey' in a:
        talk('hi can i help')
        break
# talk('how may i help you today')

# inital = listen()

# for i in skill:
#     if i in inital:
#         val = skill.get(i,'there is no skill here')
#         val()


