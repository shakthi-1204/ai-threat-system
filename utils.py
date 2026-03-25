import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak_alert(attack):
    if attack != "Normal":
        engine.say(f"Warning! {attack} detected")
    else:
        engine.say("System is safe")
    engine.runAndWait()