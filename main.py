"""
Application created by BogdosDev
name: Password Manager
version: 1.0 
"""

import json
import tkinter as tk
from tkinter import RAISED

# Colors
class Colors():
    background = '#1e1e1e'
    foreground = '#fffc94'
    active = '#dcce80'
    active_font = '#ffffff'
    dark_text = '#1F1E1C'



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title("Password Manager")
        self.resizable(height = False, width = False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        canvas = tk.Canvas(self, width=320, height=480, bg=Colors.background, highlightthickness=0)
        canvas.grid(rowspan=5)
        
        title = tk.Label(self, text="Menu", fg=Colors.foreground, bg=Colors.background, font=("Arial Bold", 32))
        title.grid(row=0)
        
        trademark = tk.Label(self, text="by Alex Bogdos", fg='#454545', bg=Colors.background, font=("Arial light", 8))
        trademark.place(x=232, y=456)

        def create_button(text, command):
            return tk.Button(self, text=text, command=command, relief=RAISED, activebackground=Colors.active, activeforeground=Colors.active_font, borderwidth = 0,bg=Colors.foreground, fg='#303030', font=("Arial Light", 14))

        # save button
        save_btn = create_button(text="Save Passwords", command=lambda: master.switch_frame(PageOne))
        save_btn.place(x=55, y=180, width=210, height=46)

        # load buton
        load_btn = create_button(text="Load Passwords", command=lambda: master.switch_frame(PageTwo))
        load_btn.place(x=55, y=240, width=210, height=46)

        # quit button
        def quit_app():
            self.quit()

        quit_btn = create_button(text="Quit", command=lambda:quit_app())
        quit_btn.place(x=110, y=400  ,width=100, height=32)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        canvas = tk.Canvas(self, width=320, height=480, bg=Colors.background, highlightthickness=0)
        canvas.grid(rowspan=5)
        
        title = tk.Label(self, text="Save", fg=Colors.foreground, bg=Colors.background, font=("Arial Bold", 32))
        title.grid(row=0)

        def create_button(text, command):
            return tk.Button(self, text=text, command=command, relief=RAISED, activebackground=Colors.active, activeforeground=Colors.active_font, borderwidth = 0,bg=Colors.foreground, fg='#303030', font=("Arial Light", 14))

        def create_entry():
            return tk.Entry(self, background=Colors.foreground, foreground=Colors.dark_text, font=("Arial Light", 11))
        
        def create_label(text):
            return tk.Label(self, text=text, fg=Colors.foreground, bg=Colors.dark_text, font=("Arial Bold", 13))
        
        # key entry
        label_key = create_label("Key").place(x=26, y=156, width=40, height=20)
        entry_key = create_entry()
        entry_key.place(x=30, y=178, width=260, height=32)
        
        # password entry
        label_pswrd = create_label("Password").place(x=20, y=226, width=100, height=20)
        entry_pswrd = create_entry()
        entry_pswrd.place(x=30, y=248, width=260, height=32)

        def save_back():
            # save to file
            if entry_key.get() != "" and entry_pswrd.get() != "":
                print(f"\nKey: {entry_key.get()}\nPassword: {entry_pswrd.get()}")
                
                with open('passwords.json', 'r') as file:
                    data = json.load(file)
                data[str(entry_key.get())] = str(entry_pswrd.get())
                with open('passwords.json', 'w') as f:
                    json.dump(data, f)
            
            master.switch_frame(StartPage)
        
        # back button
        quit_btn = create_button(text="Save & Back", command=lambda:save_back())
        quit_btn.place(x=95, y=400  ,width=130, height=32)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        canvas = tk.Canvas(self, width=320, height=480, bg=Colors.background, highlightthickness=0)
        canvas.grid(rowspan=5)
        
        title = tk.Label(self, text="Load", fg=Colors.foreground, bg=Colors.background, font=("Arial Bold", 32))
        title.grid(row=0)

        def create_button(text, command):
            return tk.Button(self, text=text, command=command, relief=RAISED, activebackground=Colors.active, activeforeground=Colors.active_font, borderwidth = 0,bg=Colors.foreground, fg='#303030', font=("Arial Light", 14))

        list_box = tk.Listbox(background=Colors.foreground, foreground='#000000', highlightthickness=0,borderwidth=0, font=("Arial", 9))
        list_box.place(x=5, y=120, width=310, height=240)
        
        with open('passwords.json', 'r') as file:
            data = json.load(file)
        
        index = 0
        for key in data:
            list_box.insert(index, key)
            list_box.insert(index + 1, data[key]) 
            list_box.insert(index + 2, "\n")
            index += 3

        # quit button
        quit_btn = create_button(text="Back", command=lambda:master.switch_frame(StartPage))
        quit_btn.place(x=110, y=400  ,width=100, height=32)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
