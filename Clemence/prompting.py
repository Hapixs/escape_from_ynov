import time

def prompting(text):
    for lettre in text: 
        print(lettre, end='', flush=True)
        time.sleep(0.03)