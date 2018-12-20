__author__ = "Egor Antonovich"
__version__ = "1.0.0"
__maintainer__ = "Egor Antonovich"
__email__ = "antonovich.egor1@gmail.com"


"""
The program will voice the time.
User input time in format "hours minutes" for example "12 20".
And program voice this time like as "twelve hours and twenty minutes" in Russian.
Program read json file which contain paths to audio files and than voice time-equivalent audio tracks.
Now program support only 12-hours time format.
"""

# Import library for reading json file
import json
# Import library for playing audio
import pygame
import time


def print_welcome():
    """
    Print introduction text about program to users.
    """
    print('*' + '-'*100 + '*')
    print("Welcome to AudioClock program!")
    print("Let me tell you a little bit about this program.")
    print("AudioClock it is a console program which can voice the input time.")
    print("How it work's: the program prompts you to enter time in the specific format and than will announce it.")
    print("Let's start to get fun!")
    print('*' + '-' * 100 + '*' + '\n')


def time_input():
    """
    Input time.
    :return: list of input values(hours and minutes).
    """
    print ("Please input time in format \"hours minutes\"")
    print ("WARNING: Program support only 12-hours time format. Be careful!")
    clock_hours, clock_minutes = map(int, raw_input("Input time:").split())
    return [clock_hours, clock_minutes]


def json_reader(data_file):
    """
    Read json file.
    :param data_file: json file which contain paths to audio files.
    :return: loaded into program json file.
    """
    with open(data_file) as json_file:
        data_sound = json.load(json_file)
    return data_sound


def clock_hours_logic_realiser(data_file, hour):
    """
    Implements the logic for finding the right path to the desired audio file based on the entered time.
    :param data_file: loaded file in json format.
    :param hour: input hours value
    :return: list of paths to audio files(time audio)
    """
    if hour == 1 or str(hour) == '0' + str(hour % 10):
        return [data_file['hours'][str(hour % 10)][0], data_file['hours'][str(hour % 10)][1]]
    elif 2 <= hour <= 4 or str(hour) == '0' + str(hour % 10):
        return [data_file['hours'][str(hour % 10)][0], data_file['hours'][str(hour % 10)][1]]
    elif 5 <= hour <= 9 or str(hour) == '0' + str(hour % 10):
        return [data_file['hours'][str(hour % 10)][0], data_file['hours'][str(hour % 10)][1]]
    elif 10 <= hour <= 12:
        return [data_file['hours'][str(hour)][0], data_file['hours'][str(hour)][1]]
    elif hour == 00:
        return [data_file['hours']['12'][0], data_file['hours']['12'][1]]


def clock_minutes_logic_realiser(data_file, minutes):
    """
    Implements the logic for finding the right path to the desired audio file based on the entered time.
    :param data_file: loaded file in json format.
    :param minutes: input minutes value
    :return: list of paths to audio files(time audio)
    """
    if minutes == 1 or str(minutes) == '0' + str(minutes % 10):
        return [data_file['minutes'][str(minutes % 10)][0], data_file['minutes'][str(minutes % 10)][1]]
    elif 2 <= minutes <= 4 or str(minutes) == '0' + str(minutes % 10):
        return [data_file['minutes'][str(minutes % 10)][0], data_file['minutes'][str(minutes % 10)][1]]
    elif 5 <= minutes <= 9 or str(minutes) == '0' + str(minutes % 10):
        return [data_file['minutes'][str(minutes % 10)][0], data_file['minutes'][str(minutes % 10)][1]]
    elif 10 <= minutes <= 20 or minutes == 30 or minutes == 40 or minutes == 50:
        return [data_file['minutes'][str(minutes)][0], data_file['minutes'][str(minutes)][1]]
    elif 21 <= minutes <= 29 or 31 <= minutes <= 39 or 41 <= minutes <= 49 or 51 <= minutes <= 59:
        return [data_file['minutes'][str(minutes / 10) + '0'][0], data_file['minutes'][str(minutes % 10)][0],
                data_file['minutes'][str(minutes % 10)][1]]
    elif minutes == 00:
        return []


def voice_time(list_of_sound):
    """
    Voice the time audio files.
    :param list_of_sound: list of paths to time audio files
    """
    for sound in list_of_sound:
        pygame.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        time.sleep(1)
        pygame.mixer.music.stop()


def main():
    """
    Entry point of the program.
    """
    try:
        print_welcome()
        timer = time_input()
        if timer[0] > 12 or timer[1] > 59:
            raise ValueError
        data = json_reader("data_dictionary.json")
        hours_audiofiles = clock_hours_logic_realiser(data, timer[0])
        minutes_audiofiles = clock_minutes_logic_realiser(data, timer[1])
        voice_time(hours_audiofiles + minutes_audiofiles)
    except ValueError:
        print ("ERROR: Incorrect time format!")


if __name__ == "__main__":
    main()
