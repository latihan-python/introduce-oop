import requests as requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)
    if(response.status_code == 200):
        print(f'sukses response : {response.status_code}')
        # print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasilpemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'oops ada kesalahan requesta {response.status_code}')

except Exception as e:
    print(f'There is an error {e}')

print('application terminated')