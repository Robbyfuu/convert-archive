import tkinter as tk
import tkinter.ttk as ttk
import jpype
import datetime
import os

from jpype import *

                # Import the module
jpype.startJVM( "-ea")




from convert import convert_excel_to_json
from tkinter import filedialog as fd
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de archivos Excel a JSON")

        self.label = tk.Label(master, text="Selecciona uno o varios archivos de Excel para convertir a JSON")
        self.label.pack()

        self.button = tk.Button(master, text="Seleccionar archivo(s)", command=self.select_files)
        self.button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.restart_button = tk.Button(self.button_frame, text="Reiniciar", command=self.restart)
        self.restart_button.pack(side="left")

        self.quit_button = tk.Button(self.button_frame, text="Cerrar", command=master.quit)
        self.quit_button.pack(side="left")

        self.treeview_frame = tk.Frame(master)
        self.treeview_frame.pack()

        self.treeview = ttk.Treeview(self.treeview_frame, columns=("name", "date"))
        self.treeview.heading("name", text="Nombre de archivo")
        self.treeview.heading("date", text="Fecha de conversión")
        self.treeview.pack()
        self.count_added_files = 0
        

    def select_files(self):
        file_paths = fd.askopenfilenames()
        if file_paths:
            for file_path in file_paths:
                try:
                    success = convert_excel_to_json(file_path)
                    if success:
                        self.status_label.config(text="Archivo convertido exitosamente")
                        self.button.config(state="disabled")
                        self.add_file_to_treeview(file_path)
                        self.count_added_files += 1
                    else:
                        self.status_label.config(text="Error al convertir archivo")
                except Exception as e:
                    print(e)
                    self.status_label.config(text="Error al convertir archivo: " + str(e))
            messagebox.showinfo("Conversión completada", f"Se han convertido {self.count_added_files} archivo(s) exitosamente a JSON")
            self.restart()
            if self.count_added_files > 0:
                self.treeview.pack()
        else:
            self.status_label.config(text="No se seleccionó ningún archivo")
        self.count_added_files = 0

    def restart(self):
        self.status_label.config(text="")
        self.button.config(state="normal")

    def add_file_to_treeview(self, file_path):
        file_name = os.path.basename(file_path)
        file_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.treeview.insert("", "end", values=(file_name, file_date))

root = tk.Tk()
app = App(root)
root.mainloop()
jpype.shutdownJVM()