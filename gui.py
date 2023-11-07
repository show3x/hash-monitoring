import tkinter as tk
from tkinter import filedialog, StringVar
import hashlib
from monitoring import calculate_hash, monitored_files

choose_hash_method = None

def hash_calculator():
    global enter_file_path, choose_hash_method  # Глобальные переменные
    if not choose_hash_method:
        return  # Защита от пустого choose_hash_method
    file_path = enter_file_path.get()
    monitored_files.append(file_path)
    hash_method = choose_hash_method.get()
    if file_path:
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
                file_hash = hashlib.new(hash_method)
                file_hash.update(data)
                hash_result_label.config(text=f'Hash ({hash_method}): ({file_hash.hexdigest()})')
        except FileNotFoundError:
            hash_result_label.config(text='File is not found')
    else:
        print('Please select a file for calculation')

def run_gui():
    
    global choose_hash_method

    root = tk.Tk()
    root.title("File hash calculator")
    root.geometry("300x250+400+200")
    root.update_idletasks()

    global enter_file_path, hash_result_label  # Глобальные переменные

    choose_hash_method = StringVar()  # choose_hash_method как StringVar
    choose_hash_method.set('md5')

    file_label = tk.Label(root, text='Select a file:')
    file_label.pack()

    enter_file_path = tk.Entry(root, width=50)
    enter_file_path.pack()

    browse_button = tk.Button(root, text='Browse', command=lambda: enter_file_path.insert(0, filedialog.askopenfilename()))
    browse_button.pack()

    hash_enter_algorithm = tk.OptionMenu(root, choose_hash_method, 'md5', 'sha1', 'sha256', 'sha512')
    hash_enter_algorithm.pack()

    calculate_button = tk.Button(root, text='Calculate hash', command=hash_calculator)
    calculate_button.pack()

    hash_result_label = tk.Label(root, text='')
    hash_result_label.pack()

    root.mainloop()

if __name__ == '__main__':
    run_gui()
