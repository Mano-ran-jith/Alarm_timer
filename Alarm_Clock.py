import pygame
import time

# Initialize the mixer module in pygame
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("alarm.mp3")

CLEAR = "\033[2J" #it's clear the terminal
CLEAR_AND_RETURN = "\033[H" # esc the looping statment to clear view

def Alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}The alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    
    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Example usage: Alarm will sound in 10 seconds
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_time = minutes * 60 + seconds
Alarm(total_time)