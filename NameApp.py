#******************************************************************************
# Author:         Noelle Landauer
# Lab:            Lab 9, CIS 133Y
# Date:           03.12.22
# Description:    UI to fetch and display historical name data
# Input:          Name, sex
# Output:         Name, sex, year, count, rank and total names
# Sources:        Lab 7, 8 & 9 specifications, Week 9 class lessons
#******************************************************************************

import pathlib
import tkinter as tk
import pygubu
from name import Name

# path to UI file
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "names.ui"

# attributes of NamesApp
class NamesApp:
    __builder = None
    __tree = None
    __mainwindow = None
    __name_entry = None
    __sex_variable = None

# run class functions
    def __init__(self, master=None):
        self.load_ui(master)
        self.setup_tree(master)
        self.fetch_data()

# build the UI
    def load_ui(self, master):
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)

        builder.import_variables(self, ['name_entry', 'sex_variable'])
        builder.connect_callbacks(self)

# build entry box & tree objects & variable for sex
        self.__name_entry = builder.get_object('name_entry', master)
        self.__sex_variable = builder.get_variable('sex_variable')
        self.__tree = self.__builder.get_object('show_tree', master)

# configure tree with 6 columns
    def setup_tree(self, master):
        tree = self.__tree
        tree.configure(columns=(0, 1, 2, 3, 4, 5), displaycolumns=(0, 2, 3, 1, 4, 5))

# column headings
        tree.heading(0, text="Name")
        tree.heading(1, text="Count")
        tree.heading(2, text="Sex")
        tree.heading(3, text="Year")
        tree.heading(4, text="Total names")
        tree.heading(5, text= "Ranking")

# column width & justification
        tree.column(0, anchor=tk.CENTER, width=150)
        tree.column(1, anchor=tk.CENTER, width=100)
        tree.column(2, anchor=tk.CENTER, width=50)
        tree.column(3, anchor=tk.CENTER, width=100)
        tree.column(4, anchor=tk.CENTER, width=100)
        tree.column(5, anchor=tk.CENTER, width=100)

# run app
    def run(self):
        self.__mainwindow.mainloop()

# callback for sex_selected radiobutton
    def sex_selected(self):
        return self.__sex_variable.get()

# turn name objects into tuple (formatting for table)
    @staticmethod
    def data_tupled(name):
        return (
            name.get_name(),
            name.get_sex(),
            name.get_year(),
            name.get_count(),
            name.get_total(),
            name.get_rank()
            )

# get the data
    def fetch_data(self):
# erase anything in tree for each round of fetching
        for i in self.__tree.get_children():
            self.__tree.delete(i)
# get name from entry box and capitalize
        name = self.__name_entry.get().capitalize()
# get sex from radiobuttons
        sex = self.__sex_variable.get()
# send name, sex to Name.readNames and get data back
        name_data = Name.readNames(name, sex)
# insert data into tree, via data_tupled()
        for i in range(len(name_data)):
             val = name_data[i]
             self.__tree.insert('', 'end', values=NamesApp.data_tupled(val),tag='odd' if (i % 2) else 'even')

# main
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Historical Name Data")
    app = NamesApp(root)
    app.run()


