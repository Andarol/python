import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup()

# Task 1
resp = requests.get('https://uk.wikipedia.org/wiki/Головна_сторінка')
with open('robots.txt', 'wb') as f:
    f.write(resp.content)

# Task 2
resp1 = 'https://www.reddit.com/r/Eldenring/comments/ygltnt/host_does_the_exact_opposite_of_what_i/'
resp1_text = requests.get(resp1).text
soup = BeautifulSoup(resp1_text, 'html.parser')
for link in soup.find_all('script'):
    print(link.get('src'))


# Task 3

def weater_api(city='London'):
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    key = 'ваш токен'

    url_link = url + 'appid=' + key + '&q=' + city


    response = requests.get(url_link).json()
    tempreture = response['main']['temp']-273
    return(f'In {city} temp is {tempreture}')
print(weater_api('Kyiv'))
