import requests
import json

TOTAL_PAGES = 2
CURRENT_COUNT = 0
FILENAME = 'get_by_id_2.json'


for i in range(1, TOTAL_PAGES + 1):
    
    # Read the existing data from the JSON file
    try:
        with open(FILENAME, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
        
    data['MAL_Pages'] += 1
    print('Page: ', i)
    params = {
        'type': 'manga',
        'page': i,
        'limit': 1
    }
    response = requests.get(
        'https://api.jikan.moe/v4/top/manga',
        params=params
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        content = response.json()
        mangas = content['data']
        
        for manga in mangas:
            attributes = {}
            
            
        # Dump the pretty-printed JSON response to a file
        # with open(FILENAME, 'w') as json_file:
        #     json.dump(content, json_file, indent=4)
        data['Manga_Count'] += 1
        
    else:
        print(f"Error: {response.status_code}")

# 47185 pages
# 50 for now