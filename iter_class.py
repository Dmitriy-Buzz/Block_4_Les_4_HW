from pprint import pprint
import json


with open('countries.json', encoding='utf-8') as c:
    countries = json.load(c)

class Wiki_countires():
    URL = 'https://wikipedia.org/wiki/'

    def __init__(self):
        return

    def __iter__(self):
        return self

    def contries_list(self):
        countries_list = []
        for i in countries:
            name_c = i['name']['common']
            countries_list.append(name_c)
        return countries_list

    def __next__(self):
        countires_dict = {}
        for name_c in self.contries_list():
            link = self.URL + name_c
            countires_dict[name_c] = link
        with open('countries_links.json', 'w', encoding='utf-8') as f:
            json.dump(countires_dict, f, ensure_ascii=False, indent=4)
            f.write('\n')












Wiki=Wiki_countires()
pprint(Wiki.__next__())