import tkinter as tk
from pynput import mouse


class JogoBatalhaNaval:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalha Naval")

        self.grid_size = 10
        self.buttons = []

        self.criar_grade()

        self.mouse_pressed = False

        self.root.bind("<Button-1>", self.iniciar_selecao)
        self.root.bind("<ButtonRelease-1>", self.finalizar_selecao)

        self.root.bind("<Enter>", self.iniciar_arrasto)
        self.root.bind("<Leave>", self.finalizar_arrasto)

    def criar_grade(self):
        for i in range(self.grid_size):
            row_buttons = []
            for j in range(self.grid_size):
                button = tk.Button(self.root, width=2, height=1, bg='white')
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def iniciar_selecao(self, event):
        self.mouse_pressed = True
        self.toggle_selecao(event)

    def finalizar_selecao(self, event):
        self.mouse_pressed = False

    def iniciar_arrasto(self, event):
        if self.mouse_pressed:
            self.toggle_selecao(event)

    def finalizar_arrasto(self, event):
        pass

    def toggle_selecao(self, event):
        widget = self.root.winfo_containing(event.x_root, event.y_root)
        if widget and widget.winfo_class() == 'Button':
            row = widget.grid_info()['row']
            col = widget.grid_info()['column']
            button = self.buttons[row][col]

            if button['bg'] == 'blue':
                button['bg'] = 'white'
            else:
                button['bg'] = 'blue'


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoBatalhaNaval(root)
    root.mainloop()
