import tkinter as tk
import time
class smoke(tk.Tk):
    def __init__(self):
        super().__init__()
        self.version = "v3.19"
        # Set the default title to 'smk'
        self.title("smk")

    def init(self):
        # 1. Set the default window dimensions (400x400)
        self.geometry("400x400")
        
        # 2. Print the static ASCII campfire/smoke display
        campfire = """
            ⢀⣀⠀⠀⠀⠀⠀⠀⠀⢱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢸⣿⡄⠀⠀⡀⠀⠀⠀⢸⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠈⢿⠇⠀⠀⣷⣦⣤⣴⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢠⣾⣷⡀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣷⣿⣿⣿⡟⢿⠿⠋⣿⣿⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣦⡀⠀⠀⢀⣿⣧⠀⠀⠀
            ⠀⠀⠀⠀⠀⢹⣿⣿⣿⠙⠻⠟⠋⠁⠀⠀⠀⠀⢿⣿⣿⣿⣶⣶⣿⣿⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⣿⣿⣿⡆⠀⠀⢀⣠⡤⠀⠀⠀⠈⠻⣿⡿⣿⣿⣿⣿⡟⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠘⠟⠋⣁⣤⡾⢟⣩⣴⣶⣆⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⠟⢉⣁⣀⣉⠀⢹⣶⣶⣤⣄⣈⡁⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⢸⣿⣿⣿⣿⢿⣿⠇⢰⡟⣫⣦⠙⢷⡀⣿⣿⣯⣍⣛⠛⠋⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠛⢋⣡⡾⠟⠋⠀⠸⣧⣙⡟⢁⡾⠁⠿⢿⣿⣿⣭⡉⠁⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠈⠙⠛⠋⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀
    
           
                                                             Smoke v3.19
                                                                               Gen1
                                                             
        """
        print(campfire)
        time.sleep(3)

    # Helper function to add the .render() method to widgets
    def _prepare_widget(self, widget):
        widget.render = widget.pack
        return widget

    # Custom Wrapper Functions
    def CreateButton(self, text, command=None, **kwargs):
        btn = tk.Button(self, text=text, command=command, **kwargs)
        return self._prepare_widget(btn)

    def CreateLabel(self, text, **kwargs):
        lbl = tk.Label(self, text=text, **kwargs)
        return self._prepare_widget(lbl)

    def CreateInput(self, **kwargs):
        entry = tk.Entry(self, **kwargs)
        return self._prepare_widget(entry)

    def GetImage(self, file_path, **kwargs):
        img = tk.PhotoImage(file=file_path, **kwargs)
        return img

    # Window termination method
    def fender(self):
        self.mainloop()

    # Starts the window loop
    def end(self):
        self.destroy()