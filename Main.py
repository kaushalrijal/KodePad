__author__ = "Kaushal Rijal"
"""
Project Name: KodePad
Project Author: Kaushal Rijal
Project Start: Sunday, October 11, 2020, 12:00 PM
Project End: 
"""

from tkinter import *

PROGRAM_NAME = "KodePad"
file_name = None

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title(PROGRAM_NAME)
        self.geometry("800x500")
        self.new_file_icon = PhotoImage(file='icons/new_file.gif')
        self.open_file_icon = PhotoImage(file='icons/open_file.gif')
        self.save_file_icon = PhotoImage(file='icons/save.gif')
        self.cut_icon = PhotoImage(file='icons/cut.gif')
        self.copy_icon = PhotoImage(file='icons/copy.gif')
        self.paste_icon = PhotoImage(file='icons/paste.gif')
        self.undo_icon = PhotoImage(file='icons/undo.gif')
        self.redo_icon = PhotoImage(file='icons/redo.gif')
        self.show_line_number = IntVar()
        self.show_cursor_info = IntVar()
        self.highlight_line = IntVar()
        self.theme_choice = StringVar()
        self.color_schemes = {
            'Default': '#000000.#FFFFFF',
            'Greygarious': '#83406A.#D1D4D1',
            'Aquamarine': '#5B8340.#D1E7E0',
            'Bold Beige': '#4B4620.#FFF0E1',
            'Cobalt Blue': '#ffffBB.#3333aa',
            'Olive Green': '#D1E7E0.#5B8340',
            'Night Mode': '#FFFFFF.#000000',
        }
        self.init_gui()

    def init_gui(self):
        self.create_menu_bar()
        self.create_shorcut_bar()
        self.create_line_number_bar()
        self.create_text_area()

    def create_menu_bar(self):
        # Menu Bar
        self.menu_bar = Menu(self)
        # File Menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", compound="left", image=self.new_file_icon, underline=0)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", compound="left", image=self.open_file_icon, underline=0)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", compound="left", image=self.save_file_icon, underline=0)
        self.file_menu.add_command(label="Save as", accelerator="Ctrl+Shift+S")

        self.file_menu.add_separator()

        self.file_menu.add_command(label="Exit", accelerator="Alt+F4")

        # Edit Menu
        self.edit_menu= Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound="left", image=self.undo_icon, underline=0, command=self.undo)
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", compound="left", image=self.redo_icon, underline=0, command=self.redo)

        self.edit_menu.add_separator()

        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", compound="left", image=self.cut_icon, underline=0, command=self.cut)
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", compound="left", image=self.copy_icon, underline=0, command=self.copy)
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", compound="left", image=self.paste_icon, underline=0, command=self.paste)

        self.edit_menu.add_separator()

        self.edit_menu.add_command(label="Find", accelerator="Ctrl+F", command=self.find_text)

        self.edit_menu.add_separator()

        self.edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all)

        # View Menu
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.show_line_number.set(1)
        self.view_menu.add_checkbutton(label="Show Line Number", variable=self.show_line_number)
        self.show_cursor_info.set(1)
        self.view_menu.add_checkbutton(label="Show Cursor Location at Bottom", variable=self.show_cursor_info)
        self.view_menu.add_checkbutton(label="Hightlight Current Line", variable=self.highlight_line)
        self.themes_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_cascade(label="Themes", menu=self.themes_menu)
        self.theme_choice.set("Default")
        for k in sorted(self.color_schemes):
            self.themes_menu.add_radiobutton(label=k, variable=self.theme_choice)

        # About Menu
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="About")
        self.about_menu.add_command(label="Help")

        # Place All The Menus
        self.config(menu=self.menu_bar)

    def create_shorcut_bar(self):
        # Shortcut Bar
        self.shortcut_bar = Frame(self, height=20, background="#00003b")
        self.shortcut_bar.pack(expand=NO, fill=X)

    def create_line_number_bar(self):
        # Line Number Bar
        self.line_number_bar = Text(self, width=2, padx=2, takefocus=0, border=0, background="#00003b", state=DISABLED, wrap=None)
        self.line_number_bar.pack(expand=NO, fill=Y, side=LEFT)

    def create_text_area(self):
        # Text Area
        self.content_text = Text(self, wrap=WORD, undo=1)
        self.content_text.pack(expand=YES, fill=BOTH)
        self.scroll_bar = Scrollbar(self.content_text)
        self.content_text.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.content_text.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)

    # Functions
    def cut(self):
        self.content_text.event_generate("<<Cut>>")

    def copy(self):
        self.content_text.event_generate("<<Copy>>")

    def paste(self):
        self.content_text.event_generate("<<Paste>>")

    def undo(self):
        self.content_text.event_generate("<<Undo>>")

    def redo(self, event=None):
        self.content_text.event_generate("<<Redo>>")
        return 'break'
    
    def select_all(self, event=None):
        self.content_text.tag_add(SEL, 1.0, END)
        return "break"

    def find_text(self, event=None):
        self.search_toplevel = Toplevel(self)
        self.search_toplevel.title("Find Text")
        self.search_toplevel.transient(self)
        self.search_toplevel.resizable(False, False)
        Label(self.search_toplevel, text="Find All: ").grid(row=0, column=0, sticky="e")
        search_entry_widget = Entry(self.search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky="we")
        search_entry_widget.focus_set()
        self.ignore_case_value = IntVar
        Checkbutton(self.search_toplevel, text="Ignore case value", variable=self.ignore_case_value).grid(row=1, column=1, sticky=E, padx=2, pady=2)
        Button(self.search_toplevel, text="Find", underline=0, command=lambda: self.search_output(search_entry_widget.get(), self.ignore_case_value.get(), self.content_text, self.search_toplevel, self.search_entry_widget)).grid(row=2, column=2, sticky="e" + "w", padx=2, pady=2)
        def close_search_widow():
            self.content_text.remove_tag(MATCH, 1.0, END)
            self.search_toplevel.destroy()
            self.search_toplevel.protocol(WM_DELETE_WINDOW, close_search_widow)
            return "break"

    def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
        content_text.remove_tag(MATCH, 1.0, END)
        self.matches_found = 0
        if needle:
            self.start_pos = 0
            while True:
                self.start_pos = content_text.search(needle, self.start_pos, nocase=if_ignore_case, stopindex=END)
                if not self.start_pos:
                    break
                self.end_pos = f"{start_pos} + {len(needle)}c"
                content_text.tag_add(MATCH, self.start_pos, self.end_pos)
                self.matches_found += 1
                self.start_pos = self.end_pos
            content_text.tag_config(MATCH, foreground="Blue", background="Green")
        search_box.focus_set()
        search_toplevel.tilte(f"{self.matches_found} matches found")

    # Keyboard Bindings
    def bind_keys(self):
        self.content_text.bind("<Control-a>", self.select_all)
        self.content_text.bind("<Control-A", self.select_all)
        self.content_text.bind("<Control-f", self.find_text)
        self.content_text.bind("<Control-F", self.find_text)


if __name__ == "__main__":
    win = App()
    win.mainloop()