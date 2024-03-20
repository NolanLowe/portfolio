from morse import Morse
import pandas as pd
import tabulate

morse = Morse()

print("Welcome to the morse code translator!\n")
while True:
    message = input("Enter your message, or Q to quit:")
    if message.lower().strip() == 'q':
        print("Goodbye.")
        quit(0)

    print(morse.to_morse(message))



