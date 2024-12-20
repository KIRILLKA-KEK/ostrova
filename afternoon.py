from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://ski-gv.ru/weather/1/').text  # получаем html код сайта
soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

links = soup.find_all('div', class_='weather-data')  # получаем список ссылок и наименований
for i, link in enumerate(links):
    condition = soup.find_all("span", class_="weather-condition")[i].text()  # извлекаем цену
    temperatura = soup.find_all("p", class_="weather-card__temp temp")[i].text()
    veter = links[1].text().split()[3:]
    # print(temperatura)
    # print(*veter)
    break
icons= soup.find_all('div', class_='weather-card weather-card_type_full weather__current-part mobile-hidden')
for i, link in enumerate(icons):
    weather_now_icon = soup.find_all("img", class_="weather-card__icon icon")[i]
    wni = weather_now_icon.get("src")
    # print(wni)
    break
params = soup.find_all('ul', class_='weather-card__params params')
for i,link in enumerate(params):
    norm_params = params[i].text()
    vosxod = norm_params.split()[0][6:]
    zaxod = norm_params.split()[1][5:]
    vlazhn = norm_params.split()[2][9:]
    davlenie = norm_params.split()[3][8:]
    # print(vosxod)
    # print(zaxod)
    # print(vlazhn)
    # print(davlenie)
    break