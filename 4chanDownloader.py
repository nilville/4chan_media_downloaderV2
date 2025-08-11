import requests
from bs4 import BeautifulSoup
import lxml
import os

print(r"""
  _  _      _____ _                        __  __          _ _         _____                      _           _           
 | || |    / ____| |                      |  \/  |        | (_)       |  __ \                    | |         | |          
 | || |_  | |    | |__   __ _ _ __   ___  | \  / | ___  __| |_  __ _  | |  | | _____      ___ __ | | ___   __| | ___ _ __ 
 |__   _| | |    | '_ \ / _` | '_ \ / _ \ | |\/| |/ _ \/ _` | |/ _` | | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _ \ '__|
    | |   | |____| | | | (_| | | | |  __/ | |  | |  __/ (_| | | (_| | | |__| | (_) \ V  V /| | | | | (_) | (_| |  __/ |   
    |_|    \_____|_| |_|\__,_|_| |_|\___| |_|  |_|\___|\__,_|_|\__,_| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\___|_|   
         ______     __        _ _       _ _ _        _    _          _    _                                               
        |  _ \ \   / /       (_) |     (_) | |      | |  | |        | |  | |                                              
        | |_) \ \_/ /   _ __  _| |_   ___| | | ___  | |  | |_      _| |  | |                                              
        |  _ < \   /   | '_ \| | \ \ / / | | |/ _ \ | |  | \ \ /\ / / |  | |                                              
        | |_) | | |    | | | | | |\ V /| | | |  __/ | |__| |\ V  V /| |__| |                                              
        |____/  |_|    |_| |_|_|_| \_/ |_|_|_|\___|  \____/  \_/\_/  \____/                                               
                                                                                                                          
                                                                                                                          
""")

url = input('Type your threade link here : ')

if not url.startswith('https://boards.4chan.org/'):
    print("Please enter a valid URL starting with 'https://boards.4chan.org/'")
    exit()
    
page = requests.get(url)

def chan(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    media = soup.find_all('a', class_='fileThumb')
    for i in media:
        media = f"https:{i.get('href')}"
        folder_path = '4chanMedia'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        response = requests.get(media)
        if response.status_code == 200:
            file_name = os.path.join(folder_path, media.split('/')[-1])
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {media}")

chan(page)