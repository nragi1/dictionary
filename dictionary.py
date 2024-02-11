import click
import json
import requests

@click.command()
@click.option('--word', prompt='Enter a word')

def dictionary(word):
    URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Word: {word}")
        print(f"Meaning: {data[0]['meanings'][0]['definitions'][0]['definition']}")
        
    elif response.status_code != 200:
        print("Sorry, there was an error. Please try again.")
        print(f"Status code: {response.status_code}")
    else:
        print(f"Sorry, the word {word} is not in the dictionary")
    

if __name__ == '__main__':
    print("Welcome to my dictionary app!")
    dictionary()