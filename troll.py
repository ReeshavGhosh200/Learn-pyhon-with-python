import time
import tkinter as tk
from tkinter import colorchooser
import pygame
pygame.mixer.init()

delay2 = 0.05
file = './Troll/a.mp3'
get = './Troll/get.mp3'

def play(file):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error playing {file}: {e}")

print("")
def startApp():
    def pick_color():
        color_code = colorchooser.askcolor(title="Choose a color")
        play(file)
        print(f"You have selected: {color_code[1]}")

    root = tk.Tk()
    root.title("Color Picker App")

    root.geometry("300x200")

    button = tk.Button(root, text="Pick a Color", command=pick_color)
    button.pack(pady=50)

    root.mainloop()

delay = 2
print("Welcome to Python Tutorial 101!")
time.sleep(10)
print("This will improve your Python skills from")
print("absolute zero to insanely advanced!")
time.sleep(delay)
print("So let's begin!")
time.sleep(delay)
print("print() Statement")
print("The print() statement is used to print values to the Python console")
time.sleep(delay)
print('The output of print("Hello World!") will be')
print("")
print("Hello World!")
print('')
time.sleep(delay)
print("Assess your learning")

ans = input("___ statement is used to print values to the console: ")

if ans == "print()" or ans == "print":
    print("Correct!")
    time.sleep(delay)
else:
    print("Try Again!")

print("Now let's go a bit advanced")
time.sleep(delay)
print("Color picker app with GUI!")
time.sleep(delay)
print("Lets see the final result before starting!")
play(file)

startApp()
print("")
print("import tkinter as tk")
play(file)
time.sleep(delay2)

print("from tkinter import colorchooser")
time.sleep(delay2)

print("")
time.sleep(delay2)

print("def pick_color():")
time.sleep(delay2)

print("    color_code = colorchooser.askcolor(title='Choose a color')")
time.sleep(delay2)

print("    print(f'You have selected: {color_code[1]}')  # color_code[1] is the hex color code")
time.sleep(delay2)

print("")
time.sleep(delay2)

print("# Create the main window")
time.sleep(delay2)

print("root = tk.Tk()")
play(file)
time.sleep(delay2)

print("root.title('Color Picker App')")
time.sleep(delay2)

print("")
time.sleep(delay2)

print("# Set window size")
time.sleep(delay2)

print("root.geometry('300x200')")
time.sleep(delay2)

print("")
time.sleep(delay2)

print("# Create a button to trigger the color picker")
play(file)
time.sleep(delay2)

print("button = tk.Button(root, text='Pick a Color', command=pick_color')")
time.sleep(delay2)

print("button.pack(pady=50)")
time.sleep(delay2)

print("")
time.sleep(delay2)

print("# Run the application")
time.sleep(delay2)

print("root.mainloop()")
play(file)
time.sleep(delay2)

play(file)
time.sleep(delay)

print("Assessment")
print("Which library was used in the following code?")
a = input("> ")
if a == "tk inter" or "tk":print("Correct!")
else: print("Wrong!")
print("Why?")
b = input("> ")
if b == "idk": 
    print("Correct!")
    play(get)
else: print("Wrong")
time.sleep(delay)
print("Congrats on you'r python mastery!")
play(get)
time.sleep(delay)
print("End")