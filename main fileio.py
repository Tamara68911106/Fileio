fron tkinter import*
from tkinter import filedialog as fd
from tkinter import ttk
import requests

def upload(): #создаем функцию
    filepath = fd.askopenfilename() # получаем путь к файлу через файлдиалог
    if filepath:
        files = {'file': open(filepath, 'rb')}
        response = requests.post('https://file.io', files=files)
        if response.status_code ==200:
            link = response.json()['link']
            entry.insert(0,link)

window=Tk()
window.title("Сохранение файла в облаке")
window.geimetry("400x200")


button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()


entry=ttk.Entry() # поле воода, куда будет выведена ссылка на наш загруженный файл,
#чтобы можноь было выделить и скопировать
entry.pack()

window.mainloop()