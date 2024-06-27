from customtkinter import *
from tkinter import filedialog, messagebox
from LanguageSymbols import palabrasReservadas
from re import escape
from parserUnificado import parserUnificado
from Preprocesador import preprocess


# This class contains every button inside the top bar of the ide
class TopBar(CTkFrame):
    def __init__(self,
                 master,
                 row,
                 column,
                 buttons_text,
                 buttons_commands,
                 padding_x=0,
                 padding_y=0):
        super().__init__(master, fg_color="transparent")

        self.grid(row=row, column=column, sticky="news", padx=padding_x, pady=padding_y)
        self.columnconfigure((0, 1), weight=0)
        self.rowconfigure(0, weight=1)

        buttons = []
        for i, value in enumerate(buttons_text):
            new_button = CTkButton(self, text=value, command=buttons_commands[i])
            buttons.append(new_button)
            new_button.grid(row=row, column=i, padx=10, sticky="w")


# This class allows the keyword highlight inside the textbox
class TextEntry(CTkTextbox):
    def __init__(self,
                 master,
                 row,
                 column,
                 padding_x=0,
                 padding_y=0):
        super().__init__(master, fg_color="#4c5b61")
        self.grid(row=row, column=column, columnspan=3, sticky="news", padx=padding_x, pady=padding_y)
        self.tag_config(tagName="Keywords", foreground="#92C897")
        self.bind("<KeyRelease>", self.apply_tags_to_keywords)

    def apply_tags_to_keywords(self, _=None):
        self.tag_remove("Keywords", "1.0", "end")
        self.__apply_tags([palabrasReservadas.values()], ["Keywords"])

    def __remove_tags(self, tag_names):
        for tag_name in tag_names:
            try:
                self.tag_remove(tag_name, "1.0", "end")
            finally:
                print(f"The tag {tag_name} wasn't found.")

    def __apply_tags(self, list_of_words, tag_names):
        if len(list_of_words) != len(tag_names):
            raise NotImplementedError
        for i in range(len(list_of_words)):
            self.__apply_tag(list_of_words[i], tag_names[i])

    def __apply_tag(self, words, tag_name):
        for word in words:
            pattern = r'\m' + escape(word) + r'\M'
            start = "1.0"
            while True:
                pos = self.search(pattern, start, stopindex="end", regexp=True)
                if not pos:
                    break
                end = f"{pos}+{len(word)}c"
                self.tag_add(tag_name, pos, end)
                start = end


# Main app class
class App(CTk):
    def __init__(self):
        super().__init__()

        self.filepath = None

        self.title("Phyton IDE")
        self.geometry("700x350")
        self.minsize(700, 350)

        self.columnconfigure((0, 1), weight=1)

        self.rowconfigure(1, weight=1)

        self.top_bar = TopBar(self, 0, 0, ["Save As", "Save", "Open", "Run"],
                              [self.save_as_file, self.save_file, self.load_file, self.parse_code],
                              15, 15)
        self.main_text_entry = TextEntry(self, 1, 0, 15, 15)

    def save_as_file(self):
        self.filepath = filedialog.asksaveasfilename(
            initialfile="my_file.phy",
            title="Save file as",
            filetypes=tuple([("Phyton file", ".phy")])
        )

        text = self.main_text_entry.get("1.0", "end-1c")

        with open(self.filepath, 'w') as f:
            f.write(text)

    def save_file(self):
        if self.filepath is None:
            self.save_as_file()

        text = self.main_text_entry.get("1.0", "end-1c")

        with open(self.filepath, 'w') as f:
            f.write(text)

    def load_file(self):
        filepath = filedialog.askopenfile(
            initialdir="/",
            title="Open file",
            filetypes=tuple([("Phyton file", ".phy")])
        )

        if filepath is None:
            raise NotImplementedError

        self.filepath = filepath.name

        with open(self.filepath, "r") as f:
            text = f.read()

        self.main_text_entry.delete("1.0", "end")
        self.main_text_entry.insert("1.0", text)
        self.main_text_entry.apply_tags_to_keywords()

    def parse_code(self):
        # Saving file is mandatory for run, as the filepath is needed
        if self.filepath is None:
            self.save_as_file()

        try:
            # preprocess text to get tokes
            text = preprocess(self.filepath)
            # call chain of responsibility with parsers here with tokens as value
            print(text)
            parserUnificado(text)
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Uncomment the following lines when not using the main file
app = App()
app.mainloop()
