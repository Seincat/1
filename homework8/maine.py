import requests
import random

def get_random_disney_character():
    total_pages = 7438
    random_page = random.randint(1, total_pages)
    page_size = 1

    url = f'https://api.disneyapi.dev/character?pageSize={page_size}&page={random_page}'
    response = requests.get(url)

    if response.ok:
        data = response.json()
        character = data['data']

        print(f"Name: {character.get('name', 'Unknown')}")
        print("Films:", ', '.join(character.get('films', [])) or "None")
        print("Short Films:", ', '.join(character.get('shortFilms', [])) or "None")
        print("TV Shows:", ', '.join(character.get('tvShows', [])) or "None")
        print("Video Games:", ', '.join(character.get('videoGames', [])) or "None")

        # Додаткова інформація (посилання та зображення)
        print(f"More info: {character.get('sourceUrl', 'No URL available')}")
        print(f"Image URL: {character.get('imageUrl', 'No Image URL available')}")

    else:
        print("Error: Unable to fetch data from Disney API.")
        print(f"HTTP Status Code: {response.status_code}")

get_random_disney_character()