import requests
from bs4 import BeautifulSoup
import lxml
import os

url = input('enter your threade link here : ')

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