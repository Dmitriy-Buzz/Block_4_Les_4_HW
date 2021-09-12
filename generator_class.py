import hashlib
import json

with open('countries_links.json', encoding='utf-8') as c:
    text = json.load(c)

def text_str():
    for line in text.items():
        yield line

for dec in text_str():
    m = hashlib.md5(b'{dec}')
    print(m.hexdigest())

