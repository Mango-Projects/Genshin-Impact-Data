import csv

with open('./food_recipes.csv', encoding='utf8') as file:
    title, *data = ['|已獲取?|'+'|'.join(i)+'|' for i in csv.reader(file)]
data = '\n'.join(data).replace('已獲取?', '<input type="checkbox" disabled>')

string = f'# 食譜\n\n{title}\n|:-:|---|---|---|\n{data}'

with open('./README.md', 'w', encoding='utf8') as file:
    file.write(string)