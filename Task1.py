# Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте
# загрузить данные из файла


import json

data = {
  "animals": [
    {
      "id": 3,
      "type": "Parrot",
      "owner": "Johnny"
    },
    {
      "id": 3,
      "type": "Parrot",
      "owner": "Johnny"
    },
    {
      "id": 3,
      "type": "Parrot",
      "owner": "Johnny"
    }
  ]
}

with open('hw.json', 'w') as file:
    json.dump(data, file)

print(data)

with open('hw.json', 'r') as file:
    json.load(file)
print(data)
