import json
import os


history_file="test_save_history.json"

def save_history(file_path, link): # функция будет принимать путь к файлу и ссылку
    history = [] # изначально хистори - путой список
    if os.path.exists(history_file): # проверяем, что путь к файлу существует в папке
        with open(history_file, 'r') as f: # если сущ-т-открываем его для чтения
            history=json.load(f) # загружаем,что было в нашем файле
    history.append({"file_path": os.path.basename(file_path), "download_link": link}) # добавляем новую инфо в историю,
    # т.к это словарь - это{}
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def test_save_history():
    test_file_path = "test_file.txt"
    test_download_link='https://file.io/hvjhgjhglk'

    save_history(test_file_path, test_download_link) # вызывает переменную с этими параметрами и передаем в нее

    with open("test_save_history.json", 'r') as f:
        history=json.load(f)
        assert len(history)==1
        assert history[0]['file_path']==test_file_path
        assert history[0]['download_link'] == test_download_link

    os.remove('test_save_history.json')

test_save_history()