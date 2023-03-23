# Alarm clock is an app that will send notifications at the appointed time. Include music, videos, or pictures.

import time
import datetime
import os
import sys
import random
import pygame
import pygame.mixer
import pygame.time
import pygame.event
import pygame.display
import pygame.font
import pygame.image
import pygame.transform
import pygame.draw
import pygame.key
import pygame.mouse
import pygame.joystick
import pygame.sprite
import pygame.surface
import pygame.rect
import pygame.mixer_music


# Set the time for the alarm
alarm_time = input("Enter the time for the alarm to go off (HH:MM:SS): ")

# Set the alarm sound
alarm_sound = input("Enter the sound file path: ")

# Set the snooze time
snooze_time = input("Enter the time for the snooze to go off (HH:MM:SS): ")

# Set the snooze sound
snooze_sound = input("Enter the sound file path: ")

# Set the alarm message
alarm_message = input("Enter the message for the alarm: ")

# Set the snooze message
snooze_message = input("Enter the message for the snooze: ")

# Set the alarm
def set_alarm(alarm_time, alarm_sound, alarm_message):
    # Convert the alarm time from string to datetime object
    alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")

    # Get the current time of the user
    current_time = datetime.datetime.now()

    # Calculate the number of seconds until alarm goes off
    time_diff = alarm_time - current_time

    # If time difference is negative, set alarm for next day
    if time_diff.days < 0:
        time_diff = time_diff + datetime.timedelta(days=1)

    # Calculate the number of seconds until alarm goes off
    secs = time_diff.seconds

    # Sleep until the alarm goes off
    time.sleep(secs)

    # Play the sound file
    pygame.mixer.init()
    pygame.mixer.music.load(alarm_sound)
    pygame.mixer.music.play()

    # Display the message
    print(alarm_message)

    # Wait for the user to stop the alarm
    stop_alarm = input("Enter 'Stop' to stop the alarm: ")

    # If the user enters stop, stop the alarm
    if stop_alarm == "Stop":
        pygame.mixer.music.stop()

# Set the snooze
def set_snooze(snooze_time, snooze_sound, snooze_message):
    # Convert the snooze time from string to datetime object
    snooze_time = datetime.datetime.strptime(snooze_time, "%H:%M:%S")

    # Get the current time of the user
    current_time = datetime.datetime.now()

    # Calculate the number of seconds until snooze goes off
    time_diff = snooze_time - current_time

    # If time difference is negative, set snooze for next day
    if time_diff.days < 0:
        time_diff = time_diff + datetime.timedelta(days=1)

    # Calculate the number of seconds until snooze goes off
    secs = time_diff.seconds

    # Sleep until the snooze goes off
    time.sleep(secs)

    # Play the sound file
    pygame.mixer.init()
    pygame.mixer.music.load(snooze_sound)
    pygame.mixer.music.play()

    # Display the message
    print(snooze_message)

    # Wait for the user to stop the snooze
    stop_snooze = input("Enter 'Stop' to stop the snooze: ")

    # If the user enters stop, stop the snooze
    if stop_snooze == "Stop":
        pygame.mixer.music.stop()


# Run the alarm and snooze
set_alarm(alarm_time, alarm_sound, alarm_message)
set_snooze(snooze_time, snooze_sound, snooze_message)
