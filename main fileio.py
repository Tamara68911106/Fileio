from tkinter import*
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import pyperclip
import json
import os

history_file= "upload_history.json"

def save_history(file_path, link): # функция будет принимать путь к файлу и ссылку
    history = [] # изначально хистори - путой список
    if os.path.exists(history_file): # проверяем, что путь к файлу существует в папке
        with open(history_file, 'r') as f: # если сущ-т-открываем его для чтения
            history=json.load(f) # загружаем,что было в нашем файле
    history.append({"file_path": os.path.basename(file_path), "download_link": link}) # добавляем новую инфо в историю,
    # т.к это словарь - это{}
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)

def upload(): #создаем функцию
    try:
        filepath = fd.askopenfilename() # получаем путь к файлу через файлдиалог
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status() # срочка позволит выявить наличие ошибок
                link = response.json()['link']
                entry.delete(0,END)
                entry.insert(0,link)
                pyperclip.copy(link)
                save_history(filepath, link)
                mb.showinfo("Ссылка скопирована", f"Ссылка {link} успешно скопирована в буфер обмена")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def show_history():
    if not os.path.exist(history_file):
        mb.showinfo("Ошибка", "История загрузок пуста")
        return

    history_window = Toplevel(window)
    history_window.title("История загрузок")

    files_listbox = Listbox(history_window, width=50, height=20)
    files_listbox.grid(row=0, column=0, padx=(10,0), pady=10)

    links_listbox = Listbox(history_window, width=50, height=20)
    links_listbox.grid(row=0, column=1, padx=(0, 10), pady=10)

    with open(history_file, 'r') as f:# открывает файл для чтения
        history=json.load(f)
        for item in history: # в цикле перебрать весь json
            files_listbox.insert(END, item['file_path'])# вставляем в конец из item, выбираем по ключу file_path
            links_listbox.insert(END, item['download_link'])


window=Tk()
window.title("Сохранение файла в облаке")
window.geometry("400x200")


button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()


entry=ttk.Entry() # поле воода, куда будет выведена ссылка на наш загруженный файл,
#чтобы можноь было выделить и скопировать
entry.pack()

history_button=ttk.Button(text="Показать историю", command=show_history)
history_button.pack()

window.mainloop()