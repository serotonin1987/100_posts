import requests
import os
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    folder_name = "json_posts"
    os.makedirs(folder_name, exist_ok=True)

    for obj in data:
        file_path = os.path.join(folder_name, f"post_{obj['id']}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(obj, f, indent=4, ensure_ascii=False)

    print(f"Сохранено {len(data)} файлов в папку '{folder_name}'.")

else:
    print("Ошибка при загрузке данных:", response.status_code)
