
import os
import subprocess
import tkinter as tk
from tkinter import ttk
from indexing import getConfigFiles


class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Config Finder')
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        self.tree = ttk.Treeview(self.root, columns=('path'))
        self.tree.heading('#0', text='File Name')
        self.tree.heading('path', text='Path')
        self.tree.column('#0', width=200)
        self.tree.column('path', width=300)

        self.tree.bind('<Double-1>', self.onDoubleClick)

        self.tree.pack(expand=True, fill='both')

        self.populateTree()

        self.root.mainloop()

    def populateTree(self):
        for file in getConfigFiles():
            self.tree.insert(
                '', 'end', text=os.path.basename(file), values=(file))

    def onDoubleClick(self, event):
        item = self.tree.focus()
        path = self.tree.item(item, 'values')[0]
        if os.path.exists(path):
            subprocess.run(['xdg-open', os.path.dirname(path)])


if __name__ == '__main__':
    app = Application()
