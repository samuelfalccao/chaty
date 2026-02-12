import pyttsx3
import os
import time

def bela(text: str):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sec(seconds: int):
    time.sleep(seconds)

print("Hello, my name is Bela. Please tell me your name.")
bela("Hello, my name is Bela. Please tell me your name.")
name = input("> ").strip()
clear()
sec(3)

print(f"Welcome, {name}, it's great to see you here")
bela(f"Welcome, {name}, it's great to see you here")
clear()
sec(3)

print("How are you?")
bela("How are you?")

current_situation = input("\n A. I'm fine! \n B. I'm really happy! \n C. I'm not feeling well today. \n D. I'm so so \n")

match current_situation:
    case "a" | "A":
        print("hmmm! ")
        bela("")
    case "b" | "B":
        print("")
        bela("")
    case "c" | "C":
        print("")
        bela("")
    case "d" | "D":
        print("")
        bela("")
