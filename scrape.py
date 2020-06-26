import requests

import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news?p=1')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
mega_links = links + links2
mega_subtext = subtext + subtext2


def sorting(list):
    sorted_list = sorted(list, key=lambda k: k['votes'], reverse=True)
    return sorted_list


def get_from_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorting(hn)


pprint.pprint(get_from_hn(mega_links, mega_subtext))
