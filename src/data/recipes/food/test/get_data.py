import csv
import json
import re

import requests as req
from bs4 import BeautifulSoup as BS
from rich import print

url = r'https://wiki.biligame.com/ys/食物一览'
html = req.get(url).text.encode().decode()

# with open('./src/data/recipes/food/test/output.html', 'r', encoding='utf8') as file:
#     html = file.read()
bs = BS(html, 'html.parser')

table = bs.find(id='CardSelectTr')
# with open('./src/data/recipes/food/test/output.html', 'w', encoding='utf8') as file:
#     file.write(str(table.prettify()))

regex = '正常料理|饮品|活动料理|特殊料理' + '|' + '减少严寒消耗|减少体力消耗|不可制作|复活|恢复体力|恢复血量|持续恢复|提升攻击|提升伤害|提升暴击|提升护盾|提升治疗效果|提升防御|生命上限提升'
data = []
for tr in table.select('tr'):
    # if not tr:
    #     continue
    tr_lst = []
    for idx, tdh in enumerate(tr.select('td,th')):
        if tdh.name == 'th':
            v = tdh.text.removesuffix('\n')
        elif idx == 0:
            v = tdh.find('img')['src'].removeprefix('https://patchwiki.biligame.com/images/ys/thumb/').removesuffix('.png')
        elif idx == 2:
            v = tdh.find('img')['alt'][0]
        elif idx == 3 or idx == 4:
            v = '|'.join(re.findall(regex, tdh.text.removesuffix('\n')))
        else:
            v = tdh.text.removesuffix('\n')
        tr_lst.append(v)
    data.append(tr_lst)

# data = [[txt for td in tr.select('td') if (txt:=td.text.removesuffix('\n'))] for tr in table.select('tr') if tr]
with open('./src/data/recipes/food/test/output.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

with open('./src/data/recipes/food/test/output.csv', 'w', encoding='utf8') as file:
    cw = csv.writer(file)
    cw.writerows(data)

"""
icon url format: f"https://patchwiki.biligame.com/images/ys/thumb/{content}.png"
"""