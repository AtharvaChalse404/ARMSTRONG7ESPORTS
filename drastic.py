import time
import random
import os
import sys
from playsound import playsound  # For Windows sound effects

# Function to print colorful text
def print_colorful(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Function to simulate dramatic typing
def dramatic_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Function to play sound effects (Windows)
def play_sound(sound_file):
    try:
        playsound(sound_file)
    except Exception as e:
        print(f"Sound error: {e}")  # Fallback if sound fails

# The most intense nuclear launch calculation ever
def nuclear_launch_calculation():
    print_colorful("\n=== INITIATING NUCLEAR LAUNCH SEQUENCE ===", "1;33")
    time.sleep(2)
    
    print_colorful("\nActivating primary ignition systems...", "1;36")
    play_sound("ignition.mp3")  # Sound effect for ignition
    time.sleep(1.5)
    
    print_colorful("\nBooting up launch control AI...", "1;35")
    play_sound("boot.mp3")  # Sound effect for booting
    time.sleep(1.5)
    
    print_colorful("\nCalibrating trajectory coordinates...", "1;34")
    play_sound("calibrate.mp3")  # Sound effect for calibration
    time.sleep(1.5)
    
    print_colorful("\nEngaging fuel pumps...", "1;32")
    play_sound("fuel.mp3")  # Sound effect for fuel pumps
    time.sleep(1)
    
    print_colorful("\nWARNING: LAUNCH SEQUENCE IRREVERSIBLE", "1;31")
    play_sound("warning.mp3")  # Sound effect for warning
    time.sleep(2)
    
    print_colorful("\nCalculating 1 + 1...", "1;37")
    for i in range(5, 0, -1):
        print_colorful(f"{i}...", "1;31")
        play_sound("countdown.mp3")  # Sound effect for countdown
        time.sleep(1)
    
    # ASCII art for extra drama
    print_colorful(r"""
      ____                  _      
     / ___| _   _  ___ ___ | | ___ 
     \___ \| | | |/ __/ _ \| |/ _ \
      ___) | |_| | (_| (_) | |  __/
     |____/ \__,_|\___\___/|_|\___|
    """, "1;33")
    
    # The result
    print_colorful("\n*** LAUNCH CODE ACCEPTED ***", "1;35")
    play_sound("launch.mp3")  # Epic sound effect for launch
    time.sleep(2)
    
    result = 1 + 1
    dramatic_print(f"\nThe result of 1 + 1 is... {result}!", delay=0.1)
    play_sound("success.mp3")  # Sound effect for success
    
    print_colorful("\nLaunch successful. Target acquired.", "1;36")
    print_colorful("The world will never be the same again.", "1;33")

# Run the program
nuclear_launch_calculation()