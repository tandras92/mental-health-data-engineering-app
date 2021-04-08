from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    url = 'https://www.mhanational.org/issues/2020/mental-health-america-all-data'

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    data = []
    data_rankings = soup.find_all('tr', {'class': 'rankings'})

    for data_ranking in range(len(data_rankings)):
        cols = data_rankings[data_ranking].find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    result = pd.DataFrame(data, columns=['State', 'Rank', 'Percentage', 'Number'])
    result.to_csv('./datasets/mha.csv', index=False)
except IOError:
    print("can't create CSV")

# print(result)
