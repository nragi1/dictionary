import click
import json
import requests
from playsound import playsound
import os
import time

@click.command()
@click.option('--word', prompt='Enter a word')

# Function to get the meaning of a word and play the pronunciation
def dictionary(word):
    URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Word: {word}")
        print(f"Meaning: {data[0]['meanings'][0]['definitions'][0]['definition']}")
        
        # Play the pronunciation
        audio = data[0]['phonetics'][0]['audio']
        audio_file = f"{word}.mp3"
        response = requests.get(audio)
        with open(audio_file, "wb") as file:
            file.write(response.content)
            
        print("Playing the pronunciation, please wait")
        time.sleep(1)
        playsound(audio_file)
        
        # Allows the user to replay audio file once - problem with playsound library
        while True:
            user_input = input("Do you want to replay the audio file? (y/n)")
            if user_input == "y":
                print("Replaying the audio, please wait")
                with open(audio_file, "wb") as file:
                    file.write(response.content)
                playsound(audio_file)
                time.sleep(1)
                print("The audio can only be replayed once!")
                print("Deleting audio file, please don't close the app")
                os.remove(audio_file)
                time.sleep(1)
                print("Audio file deleted")
                break
            elif user_input == "n":    
                print("Deleting audio file, please don't close the app")
                os.remove(audio_file)
                time.sleep(1)
                print("Audio file deleted")
                break
            else:
                print("Invalid input, please try again")
        
    # Error handling    
    elif response.status_code != 200:
        print("Sorry, there was an error. Please try again.")
        print(f"Status code: {response.status_code}")
    else:
        print(f"Sorry, the word {word} is not in the dictionary")
    
# Run the app
if __name__ == '__main__':
    print("Welcome to my dictionary app!")
    dictionary()
    